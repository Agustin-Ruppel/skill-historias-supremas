#!/usr/bin/env python3
"""
render.py · skill historias-ig

Uso:
  python3 render.py secuencia  datos.json salida.html [--png] [--max-palabras N] [--max-cta N] [--max-caja N]
                                [--duros] [--prohibir "USD,$"] [--sin-signos]
  python3 render.py calendario datos.json salida.html [--png]

Inyecta el JSON en la plantilla de assets/ y escribe el HTML. Antes corre el LINT:

SECUENCIA (lee topes y compliance del JSON: "topes":{frame,cta,caja,duros} · "compliance":{prohibir[],sin_signos,regex[]};
           los flags de la línea de comando pisan al JSON):
  keyword en el último frame (en MAYÚSCULAS o entre comillas), ×2 y = barra de respuesta · escasez fuera del CTA
  (en WN: solo F1-F2 y CTA) · palabras por frame / CTA / caja · cajas y elementos por frame · un resaltado por caja ·
  entregable visible en los últimos 3 frames · [corchetes] sin verificar · compliance · gates · variante B
CALENDARIO:
  1 accionable por día · CTA en días seguidos fuera de WN · descanso 7+ días de las keywords de RECURSO (HR) ·
  tope de accionables por semana ("tope_accionables") · días sin nada para responder ("responder": false) ·
  keywords usadas que no están en la tabla

--png: captura full-page con Playwright/Chrome; en secuencias avisa si algún teléfono quedó con contenido cortado.
Sale con código 1 si hay ERRORES (los avisos no cortan). Con topes "duros" pasarse de palabras es ERROR.
"""
import json, re, sys, os, argparse, unicodedata, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
TEXT_TYPES = {"negra", "blanca", "crema", "amarilla"}
ACCIONABLES = {"HR", "CTA", "WN"}
ENTREGABLE_CAPTURAS = {"herramienta", "planilla", "drive", "notion", "doc", "gpt", "dm-entrega"}
ESCASEZ_RE = re.compile(
    r"(\b24\s?hs\b|\bcupos?\b|\búltim[oa]s \d+|\búltim[oa]s (cupos|lugares|espacios|plazas)|\búltimo día\b|"
    r"antes que lo baje|antes de que (suba|aumente|cierre|lo baje|me arrepienta)|\bsube (el|\d)|\baumenta\b|"
    r"hoy es el último|solo por (hoy|esta semana|\d)|sólo x \d|nunca más\)|cierra el \d|primer[ao]s \d+|\bquedan \d+ (lugares|cupos|espacios|plazas|días|dias|horas)|\bson \d+\.)",
    re.I)
TOKEN_RE = re.compile(r"[0-9A-Za-zÁÉÍÓÚÑÜáéíóúñü]+")
QUOTED_RE = re.compile(r"[\"“”«»']\s*([0-9A-Za-zÁÉÍÓÚÑÜáéíóúñü]+)\s*[\"“”«»']")


def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "") if unicodedata.category(c) != "Mn").upper()


def words(s):
    s = re.sub(r"[*\"“”«»]", " ", s or "")
    return len([w for w in s.split() if re.search(r"\w", w)])


def is_cta_tag(tag):
    tag = (tag or "").upper().strip()
    return tag == "CTA" or tag.startswith("CTA ") or tag.startswith("CTA·") or tag.endswith(" CTA")


def kw_hits(text, kw):
    """Cuenta la keyword solo cuando aparece como pedido: en MAYÚSCULAS o entre comillas.
    Devuelve (hits, difiere_en_tilde)."""
    if not kw:
        return 0, False
    nk = norm(kw)
    hits, tilde = 0, False
    clean = re.sub(r"\*", "", text or "")
    quoted_spans = []
    for m in QUOTED_RE.finditer(clean):
        if norm(m.group(1)) == nk:
            hits += 1
            quoted_spans.append(m.span(1))
            tilde |= m.group(1).upper() != kw.upper()
    for m in TOKEN_RE.finditer(clean):
        if any(a <= m.start() < b for a, b in quoted_spans):
            continue
        tok = m.group(0)
        if tok.isupper() and norm(tok) == nk:
            hits += 1
            tilde |= tok != kw.upper()
    return hits, tilde


EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF]")
FLECHAS = set("⤵⬇➡⬅👉👇↪↓→")
MULETILLAS = [r"\bchau \w+", r"\ba eso le digo\b", r"\bte cuento c[oó]mo\b", r"\bno es clickbait\b"]


def _ngrams(txt, n=7):
    w = [x for x in re.sub(r"[^\wáéíóúñü ]", " ", txt.lower()).split() if x]
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def _corpus_ngrams(n=7):
    base = os.path.join(HERE, "..", "references")
    src = [os.path.join(base, "nivel-ramiro.md")] + [os.path.join(base, "corpus", f) for f in os.listdir(os.path.join(base, "corpus")) if f.startswith("stories-")]
    grams = set()
    for s in src:
        try:
            grams |= _ngrams(open(s, encoding="utf-8").read(), n)
        except OSError:
            pass
    return grams


def lint_secuencia(d, cli):
    errs, warns = [], []
    frames = d.get("frames", [])
    tipo = (d.get("tipo") or "").upper()
    kw = (d.get("keyword") or "").strip()
    topes = dict(d.get("topes") or {})
    comp = dict(d.get("compliance") or {})
    max_frame = cli.max_palabras or topes.get("frame") or 45
    max_cta = cli.max_cta or topes.get("cta") or 45
    max_caja = cli.max_caja or topes.get("caja") or 15
    duros = cli.duros or bool(topes.get("duros"))
    prohibidos = [p.strip() for p in (cli.prohibir.split(",") if cli.prohibir else comp.get("prohibir", [])) if p and p.strip()]
    sin_signos = cli.sin_signos or bool(comp.get("sin_signos"))
    regexes = comp.get("regex", []) or []
    over = errs if duros else warns
    if not frames:
        return ["No hay frames."], warns
    last = len(frames) - 1
    kw_frames, kw_count_last, kw_tilde = [], 0, False
    todos = [("", i, f) for i, f in enumerate(frames)] + [("S", i, f) for i, f in enumerate(d.get("sueltas", []) or [])]
    for pre, i, f in todos:
        name = f"{'Suelta' if pre else 'Frame'} {i+1}"
        els = f.get("elementos", [])
        boxes = [e for e in els if e.get("t") in TEXT_TYPES]
        txt = " ".join(e.get("txt", "") for e in boxes)
        alltxt = " ".join(str(e.get("txt", "")) for e in els) + " " + " ".join(str(o) for e in els for o in (e.get("opciones") or []))
        mb = re.search(r"\[[^\]]+\]", txt)
        if mb:
            warns.append(f"{name}: hay [corchetes] en el texto en pantalla ({mb.group(0)}). Dato sin verificar: completalo o sacalo antes de publicar.")
        for p in prohibidos:
            if re.search(re.escape(p), alltxt, re.I):
                errs.append(f"{name}: aparece «{p}», prohibido por el perfil (compliance).")
        for rx in regexes:
            try:
                m = re.search(rx, alltxt, re.I)
            except re.error:
                continue
            if m:
                errs.append(f"{name}: coincide con una regla del perfil «{rx}» → «{m.group(0)}».")
        if sin_signos and re.search(r"[¿¡]", txt):
            warns.append(f"{name}: usa ¿ o ¡ y el perfil los saca de pantalla.")
        if len(els) > 8:
            warns.append(f"{name}: {len(els)} elementos. Es probable que no entre en el teléfono (revisá el --png).")
        if max_caja:
            for b in boxes:
                nb = words(b.get("txt", ""))
                if nb > max_caja:
                    over.append(f"{name}: una caja tiene {nb} palabras (tope por caja {max_caja}) → «{b.get('txt','')[:45]}…»")
        if pre:
            continue
        n = words(txt)
        tag = f.get("tag") or ""
        es_cta = is_cta_tag(tag) or (i == last and tipo in ACCIONABLES)
        lim = max_cta if es_cta else max_frame
        if n > lim:
            over.append(f"{name} ({f.get('nombre','')}): {n} palabras en cajas (tope {lim}). Partilo o recortá.")
        if len(boxes) > 5:
            warns.append(f"{name}: {len(boxes)} cajas (recomendado 3-5, máx 6). ¿Hay más de una idea?")
        for b in boxes:
            if len(re.findall(r"\*[^*]+\*", b.get("txt", ""))) > 1:
                warns.append(f"{name}: una caja tiene más de un resaltado («{b.get('txt','')[:40]}…»). UNA palabra resaltada por caja.")
        hits, tilde = kw_hits(txt, kw)
        kw_tilde |= tilde
        if hits:
            kw_frames.append(i)
        if i == last:
            kw_count_last = hits
        m = ESCASEZ_RE.search(txt)
        if i != last and m and not is_cta_tag(tag):
            if tipo != "WN":
                warns.append(f"{name}: parece tener escasez fuera del frame de CTA → «{m.group(0)}». Va SOLO en el CTA (salvo WN). Si no es escasez, ignorá el aviso.")
            elif i >= 2:
                warns.append(f"{name} (WN): urgencia en un frame del medio → «{m.group(0)}». En WN abre (F1-F2) y cierra (CTA); el medio es prueba.")
    if tipo in ACCIONABLES:
        if not kw:
            errs.append(f"Secuencia {tipo} sin keyword definida.")
        elif last not in kw_frames:
            errs.append(f"La keyword «{kw}» no aparece como pedido (en MAYÚSCULAS o entre comillas) en el último frame. El CTA va al final.")
        # UNA caja de CTA por frame: dos cajas pegadas con el mismo pedido es error (el ×2 es entre flechas o en el frame siguiente)
        for i, f in enumerate(frames):
            cajas_kw = [e for e in f.get("elementos", []) if e.get("t") in TEXT_TYPES and kw_hits(e.get("txt", ""), kw)[0]]
            if len(cajas_kw) > 1:
                errs.append(f"Frame {i+1}: {len(cajas_kw)} cajas con el mismo pedido «{kw}». UNA caja de CTA (➡️ \"{kw}\" ⬅️); el re-CTA va en el frame siguiente.")
        if kw_tilde:
            warns.append(f"La keyword se escribe distinto (tilde/mayúsculas) que «{kw}». Unificala: el flow de ManyChat puede no reconocer la variante.")
        if kw and kw_frames and kw_frames[0] < last - 1 and tipo != "HR":
            warns.append(f"La keyword aparece como pedido ya en el frame {kw_frames[0]+1}. En CTA/WN el pedido va en los últimos 1-2 frames.")
        resp = [e for e in frames[last].get("elementos", []) if e.get("t") == "respuesta"]
        if not resp:
            warns.append("El frame final no tiene barra de respuesta (elemento 'respuesta').")
        elif kw:
            r = resp[0].get("txt", "").strip()
            if norm(r) != norm(kw):
                errs.append(f"La barra de respuesta dice «{r}» pero la keyword es «{kw}».")
            elif r.upper() != kw.upper():
                warns.append(f"La barra de respuesta («{r}») difiere en tilde de la keyword «{kw}».")

        def entregable(e):
            return e.get("t") in {"doc", "video"} or (e.get("t") == "captura" and (e.get("kind") or "").lower() in ENTREGABLE_CAPTURAS)
        if not any(entregable(e) for f in frames[max(0, last - 2):] for e in f.get("elementos", [])):
            if tipo == "HR":
                warns.append("HR sin entregable visible en los últimos 3 frames (doc/video o captura kind herramienta/planilla/drive/notion/gpt).")
            else:
                warns.append(f"{tipo} sin entregable visible en los últimos 3 frames (doc de entregables, PDF del programa o video). ¿Es a propósito?")
    # excesos del nivel Ramiro mal aplicado
    cajas = [e.get("txt", "") for f in frames for e in f.get("elementos", []) if e.get("t") in TEXT_TYPES]
    if cajas:
        con_emoji = [c for c in cajas if any(ch not in FLECHAS for ch in EMOJI_RE.findall(c))]
        if len(con_emoji) > len(cajas) / 2:
            warns.append(f"Emojis en {len(con_emoji)} de {len(cajas)} cajas. Cuota: como mucho 1 cada 2 cajas (el emoji es gráfico, no punto final).")
        for c in cajas:
            if re.search(r"\d", c) and any(ch not in FLECHAS for ch in EMOJI_RE.findall(c)) and not kw_hits(c, kw)[0]:
                warns.append(f"Emoji en una caja con número («{c[:40]}…»): el número ya es el golpe.")
                break
        cuenta = {}
        for c in cajas:
            for ch in EMOJI_RE.findall(c):
                if ch not in FLECHAS:
                    cuenta[ch] = cuenta.get(ch, 0) + 1
        rep_em = [f"{k}×{v}" for k, v in cuenta.items() if v > 2]
        if rep_em:
            warns.append(f"Emoji repetido más de 2 veces: {', '.join(rep_em)}.")
        todo_cajas = " ".join(cajas)
        sin_resaltado = re.sub(r"(?<![\w*])\*([^\s*][^*\n]*?)\*(?![\w*])", r"\1", todo_cajas)
        put = re.findall(r"\b\w+\*+\w*|\*+\w+\b|\w*█\w*", sin_resaltado)
        if len(put) > 1:
            warns.append(f"{len(put)} puteadas censuradas ({', '.join(put[:4])}). Máx. 1 por secuencia y solo si nombra al enemigo o es un juicio.")
        mul = [m.group(0) for rx in MULETILLAS for m in re.finditer(rx, todo_cajas, re.I)]
        if mul:
            warns.append(f"Muletillas vigiladas: {', '.join(mul)}. Máx. 1 por secuencia y no repetirla en la siguiente de la marca.")
        try:
            corpus = _corpus_ngrams()
            copiadas = [c for c in cajas if not kw_hits(c, kw)[0] and _ngrams(c) & corpus]
            for c in copiadas[:3]:
                warns.append(f"Copia textual (7+ palabras iguales a la calibración o al corpus): «{c[:60]}…». Se modela el movimiento, no el texto.")
        except Exception:
            pass
    topes_largo = {"HR": 6, "CTA": 6, "WN": 6}
    if tipo in topes_largo and len(frames) > topes_largo[tipo]:
        warns.append(f"{tipo} de {len(frames)} frames (tope {topes_largo[tipo]}; CTA 7 solo con 3 actos y capturas distintas). Juntá casos que prueban lo mismo en un frame.")

    # nivel Ramiro
    ult = frames[last].get("elementos", [])
    ult_txt = " ".join(e.get("txt", "") for e in ult if e.get("t") in TEXT_TYPES).lower()
    for e in ult:
        tx = (e.get("txt") or "").lower()
        if e.get("t") in TEXT_TYPES and tx.strip().startswith("pd") and re.search(r"\b(contame|decime|cuál|cual|qué|que|cuánt|cuant|en qué|a qué|mandame)\b", tx):
            warns.append(f"Frame {last+1}: la pd pide un dato («{e.get('txt')[:50]}»). La pd filtra o tranquiliza; la calificación va en el flow.")
    if any(e.get("t") == "doc" for e in ult) and re.search(r"\b(llamada|lo miro|lo vemos|agendamos|charlamos)\b", ult_txt):
        warns.append(f"Frame {last+1}: dos ofertas en el CTA (doc + llamada/charla). Una sola: llamada O doc.")
    todo = " ".join(e.get("txt", "") for f in frames for e in f.get("elementos", []) if e.get("t") in TEXT_TYPES)
    m = re.search(r"\bno (es|son) [^.…]{1,40}(\.\.\.|…|,)\s*(es|son)\b", todo, re.I)
    if m:
        warns.append(f"Fórmula «no es X, es Y» → «{m.group(0)}». Reencuadre Ramiro: el NO en mayúscula + la causa en la caja siguiente.")
    if len(re.findall(r"\bTU [A-ZÁÉÍÓÚa-záéíóú]+", todo)) >= 3:
        warns.append("Triada «TU X, TU Y, TU Z»: reemplazala por un concepto con nombre o un solo ejemplo concreto.")
    if tipo in {"HR", "CTA"} and not (d.get("concepto") or "").strip():
        warns.append(f"{tipo} sin 'concepto' con nombre propio (ej. «AUDIENCIA LATENTE», «HAMBRE DE LAS 11»).")
    if tipo == "HR":
        rec = d.get("recurso") or {}
        falt = [k for k in ("nombre", "volumen", "ancla") if not (rec.get(k) or "").strip()] if isinstance(rec, dict) else ["nombre", "volumen", "ancla"]
        if falt:
            warns.append(f"Recurso HR incompleto: falta {', '.join(falt)} (recurso ABISMAL = nombre · volumen · ancla · bonus).")
        tiene_bonus = "BONUS" in todo.upper() or (isinstance(rec, dict) and (rec.get("bonus") or "").strip())
        es_servicio = "AUDIT" in (str(d.get("estructura", "")) + str(d.get("meta", ""))).upper() or \
            re.search(r"(auditor|diagn[oó]stic)", str(rec.get("volumen", "") if isinstance(rec, dict) else ""), re.I)
        if not tiene_bonus and not es_servicio:
            warns.append("HR sin BONUS: si el recurso es chico (<10 ítems o <15 min), sumá un frame BONUS con «TODO JUNTO».")
    if tipo in ACCIONABLES or tipo == "PRESENTACION":
        fr0 = frames[0]
        f1 = (" ".join(e.get("txt", "") for e in fr0.get("elementos", []) if e.get("t") in {"visual", "video"}) + " " +
              " ".join(fr0.get("produccion", []) or []) + " " + str(fr0.get("hablado", "")) + " " + str(fr0.get("direccion", ""))).lower()
        if not re.search(r"(cara|gesto|mirada|lengua|ceño|boca|ojos|contrapicado|índice|indice|señal|mano|shock|asco|risa|tirad|desmay)", f1):
            warns.append("F1 sin dirección de actuación en el visual (expresión + gesto + encuadre + objeto). El gancho lo vende una cara o un absurdo.")
    ae = d.get("autoeval") or {}
    if not ae:
        warns.append("Sin 'autoeval' (juez nivel Ramiro, 8 criterios). Autoevaluá antes de entregar.")
    else:
        try:
            if float(ae.get("subiria", 0)) < 9:
                if ae.get("tope_por_insumo"):
                    warns.append(f"autoeval.subiria = {ae.get('subiria')}: topeado por insumos que faltan ({ae.get('tope_por_insumo')}). Conseguilos y sube.")
                else:
                    errs.append(f"autoeval.subiria = {ae.get('subiria')} (< 9): reescribí antes de entregar (o marcá 'tope_por_insumo' si falta un insumo real).")
        except (TypeError, ValueError):
            pass
    # hilo conductor
    if len(frames) >= 2:
        if not (d.get("hilo") or "").strip():
            warns.append("Sin 'hilo': escribí la secuencia en UNA frase (a quién + problema/afirmación + prueba + pedido) antes que los frames.")
        es_stack = "STACK" in (str(d.get("estructura", "")) + " " + str(d.get("meta", ""))).upper()
        for i, f in enumerate(frames[1:], start=1):
            if not (f.get("puente") or "").strip():
                warns.append(f"Frame {i+1}: sin 'puente' (qué pregunta/frase cortada/promesa del frame {i} contesta). Si no sale de ahí, no hay hilo.")
            boxes = [e for e in f.get("elementos", []) if e.get("t") in TEXT_TYPES]
            if boxes and not es_stack:
                first = re.sub(r'^[^\wÁÉÍÓÚÑáéíóúñ¿¡"“]+', "", boxes[0].get("txt", "")).lower()
                m = re.match(r"(otro cliente|otra clienta|otro caso|además|por otro lado|también|aparte|cambiando de tema)\b", first)
                if m:
                    errs.append(f"Frame {i+1}: arranca con «{m.group(1)}» → salto de tema. Atalo al frame anterior (pero / por eso / ¿cómo? / y el problema era…).")
                if re.search(r"\ba otr[oa]s? (le|les|cliente)\b", " ".join(e.get("txt", "") for e in boxes).lower()):
                    errs.append(f"Frame {i+1}: «a otro…» = segundo caso suelto. Mismo protagonista, o afirmación apilada (estructura STACK).")
    if not d.get("gates"):
        warns.append("Sin gates. Mínimo: flow de la keyword probado con DM de test + capturas reales.")
    if not d.get("variante_b") and not d.get("revision"):
        warns.append("Sin variante_b (otra estructura/ángulo en 3-4 líneas).")
    return errs, warns


def lint_calendario(d):
    errs, warns = [], []
    P = lambda s: datetime.date.fromisoformat(s)
    dias = sorted(d.get("dias", []), key=lambda x: x.get("fecha", ""))
    ventanas = [(P(v["desde"]), P(v["hasta"])) for v in d.get("ventanas", []) if v.get("desde") and v.get("hasta")]
    in_win = lambda f: any(a <= f <= b for a, b in ventanas)
    por_dia = {}
    for x in dias:
        por_dia.setdefault(x["fecha"], []).append(x)
    for f, xs in por_dia.items():
        acc = [x for x in xs if (x.get("tipo") or "").upper() in ACCIONABLES]
        if len(acc) > 1:
            errs.append(f"{f}: {len(acc)} accionables el mismo día. Máximo 1.")
    prev = None
    for x in dias:
        f, t = P(x["fecha"]), (x.get("tipo") or "").upper()
        if prev and t == "CTA" and prev[1] == "CTA" and (f - prev[0]).days == 1 and not (in_win(f) and in_win(prev[0])):
            warns.append(f"{prev[0]} y {f}: CTA dos días seguidos fuera de ventana WN.")
        if (x.get("responder") is False) or (x.get("responder") == ""):
            warns.append(f"{f}: el día no tiene nada para responder (regla: todos los días una historia que se pueda responder).")
        prev = (f, t)
    usos, de_recurso = {}, set()
    for x in dias:
        k = (x.get("keyword") or "").strip()
        if k:
            usos.setdefault(norm(k), []).append((P(x["fecha"]), k))
            if (x.get("tipo") or "").upper() == "HR":
                de_recurso.add(norm(k))
    for nk, lst in usos.items():
        if nk not in de_recurso:
            continue  # keyword de programa (CTA/WN: YO, INFO, sigla): se puede repetir
        lst.sort()
        for (a, ka), (b, kb) in zip(lst, lst[1:]):
            gap = (b - a).days
            if gap < 7 and not (in_win(a) and in_win(b)):
                warns.append(f"Keyword «{kb}»: {a} → {b} ({gap} días). Descanso mínimo 7 días (salvo dentro de la ventana WN).")
    tabla = {norm(k.get("kw", "")) for k in d.get("keywords", [])}
    for nk, lst in usos.items():
        if nk not in tabla:
            warns.append(f"Keyword «{lst[0][1]}» se usa en el calendario pero no está en la tabla de keywords (recurso/flow).")
    mix = d.get("mix_objetivo") or {}
    if mix:
        semanas = {}
        for x in dias:
            y, w, _ = P(x["fecha"]).isocalendar()
            semanas.setdefault((y, w), []).append(x)
        for (y, w), xs in semanas.items():
            fechas = {x["fecha"] for x in xs}
            if len(fechas) < 7 or all(in_win(P(f)) for f in fechas):
                continue  # semana parcial o semana push: no se exige la mezcla base
            cnt = {}
            for x in xs:
                t = (x.get("tipo") or "").upper()
                t = "POLL" if t == "QA" else t
                cnt[t] = cnt.get(t, 0) + 1
            for t, rango in mix.items():
                if d.get("tope_accionables") and t.upper() in ACCIONABLES:
                    continue  # el tope propio de la marca manda sobre la mezcla base
                lo = int(str(rango).split("-")[0])
                if cnt.get(t.upper(), 0) < lo:
                    warns.append(f"Semana {y}-W{w:02d}: {t} {cnt.get(t.upper(), 0)} (objetivo {rango}).")
    tope = d.get("tope_accionables")
    if tope:
        semanas = {}
        for x in dias:
            if (x.get("tipo") or "").upper() in ACCIONABLES:
                y, w, _ = P(x["fecha"]).isocalendar()
                semanas.setdefault((y, w), []).append(x["fecha"])
        for (y, w), fs in semanas.items():
            if len(fs) > int(tope) and not all(in_win(P(f)) for f in fs):
                errs.append(f"Semana {y}-W{w:02d}: {len(fs)} accionables (tope del perfil {tope}): {', '.join(fs)}.")
    return errs, warns


def inject(template_name, data):
    with open(os.path.join(ASSETS, f"{template_name}.html"), encoding="utf-8") as fh:
        tpl = fh.read()
    blob = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    out, n = re.subn(r'(<script id="data" type="application/json">)(.*?)(</script>)',
                     lambda m: m.group(1) + "\n" + blob + "\n" + m.group(3), tpl, count=1, flags=re.S)
    if n != 1:
        sys.exit("No encontré el bloque #data en la plantilla.")
    return out


def screenshot(html_path):
    try:
        import asyncio
        from playwright.async_api import async_playwright
    except Exception:
        print("· (sin Playwright: no se genera PNG)")
        return None, []
    png = os.path.splitext(html_path)[0] + ".png"
    cortados = []

    async def run():
        async with async_playwright() as p:
            try:
                b = await p.chromium.launch(channel="chrome")
            except Exception:
                b = await p.chromium.launch()
            pg = await b.new_page(viewport={"width": 1180, "height": 900})
            await pg.goto("file://" + os.path.abspath(html_path))
            await pg.wait_for_timeout(1200)
            res = await pg.evaluate("""() => [...document.querySelectorAll('.cell')].map(c => {
                const ph = c.querySelector('.phone'); const lb = c.querySelector('.label');
                return ph && ph.scrollHeight > ph.clientHeight + 2 ? (lb ? lb.innerText.split('\\n')[0] : '?') : null;
            }).filter(Boolean)""")
            cortados.extend(res)
            await pg.screenshot(path=png, full_page=True)
            await b.close()
    asyncio.run(run())
    return png, cortados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tipo", choices=["secuencia", "calendario"])
    ap.add_argument("datos")
    ap.add_argument("salida")
    ap.add_argument("--png", action="store_true")
    ap.add_argument("--max-palabras", type=int, default=None, help="tope por frame (default: topes.frame del JSON o 45)")
    ap.add_argument("--max-cta", type=int, default=None, help="tope del frame de CTA (default: topes.cta o 45)")
    ap.add_argument("--max-caja", type=int, default=None, help="tope por caja (default: topes.caja o sin tope)")
    ap.add_argument("--duros", action="store_true", help="pasarse de un tope es ERROR (regla dura del perfil)")
    ap.add_argument("--prohibir", default="", help="términos prohibidos en pantalla, separados por coma")
    ap.add_argument("--sin-signos", action="store_true", help="avisar si hay ¿ o ¡ en pantalla")
    a = ap.parse_args()
    with open(a.datos, encoding="utf-8") as fh:
        data = json.load(fh)
    errs, warns = (lint_secuencia(data, a) if a.tipo == "secuencia" else lint_calendario(data))
    for e in errs:
        print("✗ ERROR:", e)
    for w in warns:
        print("! aviso:", w)
    if not errs and not warns:
        print("✓ lint OK")
    html = inject(a.tipo, data)
    os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
    with open(a.salida, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("→ HTML:", a.salida)
    if a.png:
        png, cortados = screenshot(a.salida)
        if png:
            print("→ PNG:", png)
        for c in cortados:
            print(f"! aviso: el teléfono «{c}» tiene contenido cortado (no entra en la pantalla). Partí ese frame o sacá elementos.")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
