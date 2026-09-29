# Formatos de salida (MD + JSON del HTML)

Siempre se entregan los dos: el **.md** (se lee, se copia a IG, se versiona) y el **.html** renderizado desde el
JSON con `scripts/render.py` (lo ve el equipo o el cliente). Esquemas de JSON de ejemplo:
`assets/ejemplo-secuencia.json` y `assets/ejemplo-calendario.json`.

## 1. Calendario · `historias/calendario/AAAA-MM.md` (o `AAAA-MM-DD-semana.md`)
```markdown
# Calendario de historias · [Mes AAAA] · @[cuenta]
**Objetivo:** [conversaciones/semana, agendas, cierre de cupos] · **Modo:** [estándar] · **Ventana WN:** [26→31 · motivo real]
**Recursos activos:** KEYWORD (recurso · flow ok) · … · **Reels que empujan:** [fechas]

## Semana 1 · [fechas]
| Fecha | Día | Tipo | Estructura | Ángulo / tema | Keyword | Recurso | Fr | Hora | Nota |
|---|---|---|---|---|---|---|---|---|---|
| 01-10 | jue | PRESENTACION | PRE-QUEHAGO | qué hago para los nuevos | YO | doc entregables | 5 | 19-21 | pico de seguidores del reel del 29 |
| 02-10 | vie | HR | HR-OBJ | "no tengo tiempo para grabar" | SISTEMA | Notion del sistema | 5 | 19-21 | reel del día empuja SISTEMA |
…
**Mezcla:** HR 3/2-3 ✓ · CTA 2/2 ✓ · POLL 1/1 ✓ · keywords sin choque de descanso ✓

## Keywords del mes
| Keyword | Recurso | Flow | Usos |
## Reglas aplicadas / notas
```
JSON: `{kicker, titulo, titulo_em, meta, vista?("mes"|"semana"), ventanas[{desde,hasta,nombre}],
mix_objetivo{HR,CTA,POLL,WN}, tope_accionables?, dias[{fecha, tipo, titulo, estructura, keyword, recurso, frames,
hora, responder(true|false|"encuesta"|"caja"|"keyword"), dist?("⭐"|"⏱48h"), nota}], keywords[{kw, recurso,
flow(ok|falta|probar|a-mano), usos[]}], reglas[], notas[], pie}` · QA cuenta como POLL en la mezcla.

## 2. Secuencia del día · `historias/secuencias/AAAA-MM-DD-TIPO-KEYWORD.md`
(formato guion frame a frame: el estándar de esta skill)
```markdown
# Secuencia · [Título]
**[Día dd-mmm-aaaa] · @[cuenta] · [tipo: hand raiser / CTA / why now…] · [estructura: HR-OBJ] · keyword [KEYWORD]**
**La línea:** [la secuencia en UNA frase: a quién + problema/afirmación + prueba + pedido]
[Por qué hoy, 1-2 líneas: día del calendario, ángulo ganador, reel que empuja]. Ráfaga: los [N] frames en 10-20 min,
ideal [hora]. [KEYWORD] descansó desde el [fecha] (regla 7+ días OK).

## FRAME 1 · [nombre del beat] [HOOK GANCHO]
**En pantalla:**
- caja negra: `texto literal` (PALABRA resaltada amarillo)
- caja blanca: `texto literal`
- [captura real: qué es, qué se tacha en rojo]
**Visual:** [foto/video, cara, fondo, ancla visual, flecha neón hacia…] · **Sticker:** [si hace algo]
**Hablado (premisa, no guion):** "…" (solo si es video)
**Fallback sin captura:** [qué se hace] — no se fabrica captura.

## FRAME 2 · [nombre del beat] [TIPO]
**Viene de:** [la pregunta / frase cortada / promesa del frame 1 que este frame contesta]
**En pantalla:** …

## FRAME N · CTA [CTA]
**Viene de:** [la prueba del frame anterior → "¿querés lo mismo?"]
**En pantalla:**
- [entregable a la vista: portada/chip con NOMBRE + VOLUMEN]
- UNA caja (crema con glow o amarilla): `respondé ➡️ "KEYWORD" ⬅️ y [qué te llevás] ⤵️`
- (opcional) caja crema chica: `pd: solo si ya [filtro]` · `contesto a TODOS` — **nunca** pedir un dato
**Visual:** cara/gesto + flecha dibujada al campo de mensaje. **Música:** [concreta]

## FRAME N+1 · BONUS [CTA] (si el recurso es chico o para re-pedir)
- caja amarilla MAYÚSCULAS: `BONUS: [NOMBRE DEL BONUS]`
- caja negra: `[qué es, en una línea]`
- caja crema: `respondé "KEYWORD" y te llega TODO JUNTO ⬇️`

## Gates antes de publicar
1. Flow KEYWORD en ManyChat armado + DM de test (trigger de respuesta a historia). Sin test, el CTA se cae.
2. Capturas reales conseguidas (lista) · permisos de clientes · claims = mínimo defendible.
3. Registrar la pieza (etiqueta ManyChat / registro) al publicar.

## Reglas aplicadas
- [qué reglas del método y del perfil se usaron: escasez solo en CTA, keyword ×2, puente de aire, compliance…]

## Variante B (opcional)
[otra estructura o ángulo para el mismo día, en 3-4 líneas]
```
JSON: `{kicker, cuenta, inicial, titulo, titulo_em, meta, tipo, keyword, rafaga, hilo, concepto,
recurso{nombre, volumen, ancla, bonus}, autoeval{gancho, hilo, prueba, recurso, cta, voz, formato, subiria, notas},
chips[], frames[{nombre, tag,
puente (desde el frame 2), hora?, elementos[{t, txt, pos?, kind?, dur?, opciones?}], hablado?, produccion[]}], porque, variante_b, gates[],
reglas[], revision?{metrica, veredicto, problemas[], funciona[]}, sueltas?[frames], topes?{frame, cta, caja,
duros}, compliance?{prohibir[], sin_signos, regex[]}, pie}` (texto con `**negrita**`, `*resaltado*` y `` `código` ``)
Tipos de elemento: `negra|blanca|crema|amarilla` (texto, `*palabra*` = resaltado) · `captura` (kind: dm, whatsapp,
discord, dashboard, perfil, planilla, herramienta · txt · rows[]) · `doc` (kind: doc, loom, pdf, notion · dur) ·
`visual` (placeholder de foto) · `video` (premisa hablada · dur) · `sticker` (kind: encuesta, pregunta, slider,
countdown, link, mencion, musica · opciones[]) · `flecha` · `neon` · `respuesta` (barra con la keyword, en el CTA).

## 3. Registro · `historias/registro.md`
```markdown
| Fecha | Tipo | Estructura | Keyword | Fr | Hora | Views F1 | Views CTA | Views último | Resp. | % resp | Decay | Visitas perfil | Agendas | Calidad | Nota |
```
Debajo, cada semana: `### Lectura semana [n]` con 3-5 líneas (qué rindió vs benchmark, frame que cayó, qué se
cambia) y las actualizaciones que se pasaron al perfil.
