---
name: historias-ig
description: "Use when el usuario quiere saber QUÉ historias de Instagram subir (calendario del mes o de la semana: qué tipo de story va cada día — hand raiser, CTA, why now, encuesta, awareness, prueba social, libre) o ESCRIBIR la secuencia de stories de un día concreto frame por frame (texto por caja, visual, sticker, keyword, gates), con el método SYK / Ramiro Cubría, para su marca o la de un cliente (multi-marca, con perfil por proyecto). También registra resultados (views, respuestas, % contra benchmark) para ajustar el calendario, y revisa secuencias ya hechas. Entrega MD + HTML visual (calendario y mockups de teléfono). Trigger phrases: 'qué historias subo hoy', 'calendario de historias', 'plan de stories del mes', 'armá la secuencia de hoy', 'hand raiser', 'why now', 'secuencia de CTA', 'historias para [cliente]', 'registrá cómo fueron las historias', 'revisá esta secuencia'. NO usar para guiones de reels ni para el calendario del feed."
---

# /historias-ig — calendario y secuencias de IG Stories que abren conversaciones

```
RECIBE:   "¿qué subo?" (mes / semana / hoy) · un objetivo o idea del día · métricas de historias · capturas a revisar
HACE:     perfil de marca → calendario (tipo por día) → secuencia del día frame a frame → lint + HTML → registro y ajuste
DEVUELVE: historias/calendario/*.md+.html · historias/secuencias/*.md+.html · historias/registro.md · 1 línea de estado
NUNCA:    inventar cifras, casos, capturas o escasez · publicar · usar una keyword sin recurso y flow · copiar copy ajeno
```

**La metodología completa vive en `references/`** (método, calendario, estructuras, copy, visual, métricas). Este
archivo es el procedimiento. El corpus real (~120 secuencias transcriptas, videos, Looms, consultorías SYK) está en
`references/corpus/` con índice en `corpus/INDEX.md`.

## LA LEY
Cada día hay una historia que abre conversación. Cada secuencia cuenta **UNA sola cosa de corrido**: cada frame
contesta lo que dejó abierto el anterior, muestra una **prueba real**, entrega algo que **se ve** y pide **UNA**
cosa al final. Lo que toca cada día lo decide el calendario, no la inspiración.

## Modos (detectar y rutear)
| Si el usuario… | Modo |
|---|---|
| es la primera vez en el proyecto, o no hay perfil | **0 · PERFIL** (y después sigue con lo que pidió). En modos 2, 3 y 4 no se frena: perfil mínimo con `[asumido]` y las preguntas van al final |
| pide "calendario", "qué subo este mes/semana", "plan de stories" | **1 · CALENDARIO** |
| pide "qué subo hoy", "armá la secuencia de hoy/del jueves", trae un tema u objetivo del día | **2 · SECUENCIA** |
| pega métricas o capturas de Insights, dice "registrá" o "cómo me fue" | **3 · REGISTRO** |
| pasa capturas o el texto de una secuencia suya y pide opinión | **4 · REVISIÓN** |

"¿Qué subo hoy?" sin calendario: armar la semana en mini-calendario (7 filas, reglas de `calendario.md`), guardarla
y escribir la secuencia de hoy. Todo en el mismo turno.

## Reglas duras
1. **Nunca inventar números, casos, capturas ni escasez.** Lo que no está verificado va entre `[corchetes]` y no se
   publica. Si falta la prueba, se baja a una estructura que no la necesite o se usa el sistema propio corriendo.
   *(guiones de referencia: "NO se fabrica captura"; Cubria: "cada vez que anunciamos subida de precios, subieron".)* Si el proyecto
   dice que los números del dueño no se verifican, los que él da van tal cual; se marcan solo los que Claude
   infiere o calcula.
2. **Máximo 1 accionable (HR/CTA/WN) y 1 pedido por día.** El CTA va en el último frame (o en los últimos 2).
3. **Escasez con número solo en el frame de CTA.** Excepción WN: ahí la urgencia es el tema, así que puede abrir
   (F1: qué cambia y cuándo) y cerrar (CTA: cupos, fecha y monto si el compliance lo permite). En el medio va prueba.
4. **Keyword**: no se publica sin recurso listo y flow probado con DM de test (trigger de respuesta a historia). Si
   no hay flow y se esperan ≤20 respuestas: a mano, avisando "(las contesto yo)".
   - La keyword de **recurso** (HR) descansa 7+ días entre usos.
   - La keyword del **programa** (CTA y WN: YO, INFO, la sigla) lleva siempre al mismo doc o charla, así que se
     puede repetir. En una ventana WN se sostiene todos los días.
5. **El entregable se ve** antes del CTA o junto con él (player con duración, chip de Doc, Drive, Notion, portada).
6. **Todos los días una historia que se pueda responder** (keyword, encuesta, caja o "escribime").
7. **Se modela el molde, nunca el copy**: el texto y el tema salen de la marca, no de Cubria ni de ningún referente.
8. **Las reglas de la marca mandan sobre el método**: compliance (precio en pantalla, moneda, palabras prohibidas,
   permisos de clientes por canal), topes de palabras y **tope de accionables por semana**. Si el proyecto tiene su
   propio manual o skill de historias, sus reglas, rutas y registro ganan. Esta skill aporta el método y los moldes.
9. **Una idea por frame**, respetando el tope de palabras del perfil (default 45 por frame y 15 por caja). Cuentan
   solo las cajas de texto, no los stickers ni las capturas. Texto arriba y abajo, nunca sobre la cara.
10. **La story documenta; el reel enseña.** Si un frame necesita tres párrafos, es un reel mal ubicado.
11. **Un turno = una entrega completa**: el calendario entero, o la secuencia entera más una variante B. Si hay
    preguntas, van todas juntas, cada una con su default.
12. **Todo queda en archivos (.md + .json + .html).** En el chat va un resumen y las rutas.
13. **Hilo conductor.** Toda secuencia se resume en UNA frase (`hilo`) y sigue a un solo protagonista o a una sola
    afirmación (en WN y CTA, probada con 2-4 casos apilados). Cada frame desde el 2 contesta la pregunta, la frase cortada o la promesa del anterior (`puente`).
    Nunca "otro cliente…", "además…", ni presentarse en el medio sin que venga del frame anterior. El gancho
    también se ata con una pd o un giro (`estructuras.md` §hilo conductor). *(caso real: un "Qué hago" con 4 datos buenos pero sueltos:
    IA que llama → "soy X" → "otro cliente…" → filtro.)*

## HIDRATAR
- **Primero, ver si la marca ya tiene sistema propio**: `ls .claude/skills/ | grep -i histori` y
  `ls estrategia/ | grep -i histori` (manual de historias). Si existe, se lee entero y **manda**: su formato, sus
  rutas (p. ej. `contenido/historias/`), su registro (p. ej. `publicado.md`), sus topes y su frecuencia de pedidos.
  Se anotan en el perfil. Esta skill no crea un segundo registro paralelo.
- **Siempre, antes de preguntar nada:**
  - el perfil: `historias/perfil-marca.md` (buscar también en `contenido/historias/`)
  - `historias/registro.md` (últimas 4 semanas)
  - el calendario vigente en `historias/calendario/`
  - la fecha real: `date +%F`
- **Si no hay perfil**, el contexto del proyecto: `CLAUDE.md`, `estrategia/*` (cliente ideal, tono, casos, ángulos),
  `productos/*`, calendario de reels y flows de ManyChat documentados, y la matriz de permisos de casos (¿se pueden
  nombrar en historias?).
- **Referencias por modo** (cargar solo las que hacen falta):
  - PERFIL → `references/perfil-marca.md`
  - CALENDARIO → `references/calendario.md` + `references/metodo.md` (+ `metricas.md` si hay registro)
  - SECUENCIA → **`references/nivel-ramiro.md` (siempre, primero)** + `references/estructuras.md` (índice, árbol y
    piezas sueltas) + **solo** el archivo del tipo del día
    (`references/estructuras/hr.md` | `cta.md` | `wn.md` | `nutricion.md`) + `references/copy.md` +
    `references/visual.md`, más 1-2 ejemplos reales de la estructura elegida (`grep -i "<código|tema>"
    references/corpus/INDEX.md` y abrir esa sección)
  - REGISTRO → `references/metricas.md`
  - REVISIÓN → `nivel-ramiro.md` + `metodo.md` + `estructuras.md` + `copy.md` + `visual.md` + `metricas.md` §2-3 +
    `plantillas-output.md`
  - Formatos de salida → `references/plantillas-output.md`; esquemas JSON → `assets/ejemplo-secuencia.json`,
    `assets/ejemplo-calendario.json`

## El proceso

### 0 · PERFIL (una vez por proyecto)
1. Leer el contexto en silencio y anotar lo que ya está respondido.
2. Mandar una lista numerada con solo lo que falta, cada punto con su default (`perfil-marca.md` §Onboarding).
   Si dice "usá los defaults", o no contesta algo que no es crítico, seguir marcándolo `[asumido]`.
3. Guardar `historias/perfil-marca.md` con la plantilla. Crear también `historias/registro.md`, solo con el
   encabezado de la tabla (`plantillas-output.md` §3). Después seguir con el modo que pidió.

### 1 · CALENDARIO (mes o semana)
1. **Primero, ventanas y eventos**: WN (suba, cupos, cierre, con fecha y motivo reales), teaser o lanzamiento,
   hitos, fechas especiales, días sin grabar. Si el perfil no lo dice, es la única pregunta obligatoria:
   "¿hay suba, cupos o cierre este mes?".
2. **Modo y grilla base** (`calendario.md` §2). Aplicar las reglas del motor (§3) y el mapa del mes (§4):
   presentación o POV al arranque, encuesta de ángulos temprano, crucero, warmeo en semana 3, WN en los últimos
   5-7 días y un día de descanso después.
3. **Por día**:
   - tipo. Auditoría o diagnóstico por chat = HR; en llamada = CTA
   - código de estructura sugerida
   - ángulo o tema (de ángulos ganadores, objeciones de la semana y casos disponibles)
   - keyword (con su descanso)
   - recurso
   - N° de frames y hora
   - nota (el reel que empuja, el evento)
4. **Chequear**:
   - mezcla semanal contra el modo y el tope de accionables del perfil
   - que no haya CTAs seguidos fuera de WN ni más de 1 accionable por día
   - descanso de las keywords de recurso
   - que todos los días tengan algo para responder (campo `responder`)

   El lint de `render.py calendario` revisa todo eso. Cargar en el JSON `tope_accionables` y, por día, `recurso`,
   `responder` y `dist` (⭐ destacar / ⏱ 48 h) si aplica.
5. **Escribir el MD y el JSON, y renderizar** (ver Manos).
6. **Cerrar con "Para preparar esta semana"**: recursos, flows y capturas que faltan, con fecha límite.

### 2 · SECUENCIA DEL DÍA
1. **Tipo del día**: sale del calendario. Si no hay calendario, se decide con las reglas y se avisa.
2. **Inventario de insumos reales**:
   - resultado propio (con captura)
   - casos con permiso
   - la objeción o pregunta de la semana
   - recurso, keyword y estado del flow
   - evento
   - hook ganchos ganadores del perfil

   Si falta lo crítico, decirlo y bajar a una estructura que no lo necesite.
3. **Elegir la estructura** con el árbol de `estructuras.md`. Leer 1-2 ejemplos reales del corpus de esa estructura
   para calibrar la forma. No copiarlos.
3b. **Escribir la línea antes que los frames** (`estructuras.md` §hilo conductor):
    - `hilo` en una frase: a quién + problema o afirmación + prueba + pedido
    - el protagonista (un caso o una afirmación)
    - la cadena de puentes: qué pregunta deja abierta cada frame y cuál la contesta

    Si no entra en una frase, son dos secuencias: se elige una.
3c. **Material del nivel Ramiro** (`nivel-ramiro.md` §2), antes de redactar:
    - el número más fuerte del inventario (¿está fuera de lo normal para el avatar?) va en F1 o F2
    - un concepto con nombre propio (HR y CTA)
    - el recurso ABISMAL: nombre, volumen, ancla y bonus
    - la cara o el absurdo del F1, con dirección de actuación
    - las capturas con su texto literal y desordenado
    - el remate seco
4. **Escribir frame por frame en formato guion frame a frame** (`plantillas-output.md` §2), y en cada frame:
   - la función `[TAG]`
   - cada caja con su color y el texto literal, con UNA palabra resaltada
   - el visual y el sticker
   - el hablado si es video (premisa, no guion)
   - el fallback si no hay captura

   Sobre la secuencia:
   - en HR y CTA, F1 es un hook gancho o un hook fuerte
   - los frames intermedios empujan a la siguiente historia ("…", flecha, pregunta puente)
5. **Cierre**:
   - el CTA en UNA caja (➡️ "KW" ⬅️ o la keyword gigante), con flecha al cajón
   - el re-CTA va en el frame siguiente (BONUS o "llega al instante"), nunca en dos cajas pegadas
   - una sola oferta (llamada O doc)
   - la pd filtra o tranquiliza; nunca pide un dato
   - escasez solo si es real
   - el entregable a la vista
6. **Gates**: flow con DM de test, capturas a conseguir, permisos, claims defendibles. Agregar "Reglas aplicadas",
   "Por qué hoy" (campo `porque`) y la **Variante B** (campo `variante_b`: otra estructura u otro ángulo, en 3-4
   líneas). Si se sabe la hora de cada frame, cargarla en `hora`.
7. **JSON y render con lint**: cargar en el JSON `topes` ({frame, cta, caja, duros}) y `compliance` ({prohibir[],
   sin_signos, regex[]}) desde el perfil. Corregir todo ✗ ERROR, y los avisos que tengan sentido, antes de
   entregar.
8. **Juez adversarial** (`nivel-ramiro.md` §4):
   - Primero las 3 debilidades, después los topes automáticos y recién ahí las notas, en `autoeval` con
     `debilidades`.
   - Si hay subagentes, el juez corre en uno aparte que solo ve `nivel-ramiro.md` y la secuencia.
   - Si "¿la subiría?" queda por debajo de 9, se reescribe. Si lo que falta es un insumo real (captura, caso,
     número de resultado), se entrega con el tope marcado y se pide.
   - Test del escéptico: verificar toda cuenta en pantalla.
9. **En el chat**: 3-5 líneas de resumen, las rutas, la nota del juez y el texto de cada frame listo para copiar.

### 3 · REGISTRO
1. Pasar las métricas a una fila de `historias/registro.md` (views F1, views del frame de CTA, views del último,
   respuestas, visitas, agendas) y calcular el % de respuesta y el decay. Si vienen en capturas de Insights, leerlas.
2. Comparar con el benchmark del tipo (`metricas.md` §2) y pasar por el árbol de diagnóstico (§3): salen 1-3
   acciones concretas.
3. Actualizar los aprendizajes del perfil: hook ganchos ganadores, estructura que rinde por tipo, keyword usada y
   reglas propias con fecha.
4. **Cada semana**: escribir la "Lectura semana N" y ajustar los días siguientes del calendario. Se cambia de a una
   pieza ("nunca matar lo que funciona").

### 4 · REVISIÓN
1. **Leer lo que llega**: capturas (con Read) o texto. Identificar tipo, estructura y objetivo. **Mirar la hora de
   publicación de cada captura**: si hay más de 20 min entre frames, la ráfaga se rompió y probablemente ahí se
   perdieron respuestas. Clasificación: auditoría o regalo por chat = HR; llamada = CTA.
2. **Si hay métricas**, calcular el % y compararlo con el benchmark del tipo (`metricas.md`). Cargarlo en el
   registro (modo 3).
3. **Checklist de revisión**, frame por frame:
   - tipo claro
   - hilo: ¿se resume en una frase?, ¿cada frame sale del anterior?
   - ráfaga (horarios)
   - F1 frena el scroll y empuja
   - una idea por frame
   - prueba real
   - entregable visible
   - UN solo pedido, al final
   - keyword ×2 con flecha
   - escasez creíble, solo en el CTA (un "primeros 10" con muchas respuestas parece lleno)
   - voz y compliance

   De cada frame sale qué funciona, qué rompe y la regla que lo explica.
4. **Versión corregida en formato guion frame a frame** (MD + JSON + HTML), con el campo `revision` (métrica, veredicto,
   problemas, lo que se mantiene) para que el HTML muestre el antes y después. Se fecha en el **próximo día
   válido**: si es de recurso, la keyword con 7+ días de descanso, y sin CTA el día anterior. Se guarda en
   `historias/revisiones/AAAA-MM-DD-revision-TEMA.*`.

## Manos
```bash
SK=~/.claude/skills/historias-ig
date +%F                                                   # fecha real antes de fechar nada
python3 -c "import calendar; print(calendar.month(2026,10))"   # grilla del mes
python3 $SK/scripts/render.py calendario historias/calendario/2026-10.json historias/calendario/2026-10.html --png
python3 $SK/scripts/render.py secuencia historias/secuencias/2026-10-02-HR-SISTEMA.json \
        historias/secuencias/2026-10-02-HR-SISTEMA.html --png   # topes y compliance salen del JSON (del perfil)
open historias/secuencias/2026-10-02-HR-SISTEMA.html      # mostrarlo
grep -i "HR-OBJ\|objeción" $SK/references/corpus/INDEX.md  # ejemplos reales de una estructura
```
- `render.py` inyecta el JSON en la plantilla (`assets/secuencia.html`, `assets/calendario.html`) y corre el lint.
  - **Secuencia**:
    - keyword como pedido (en MAYÚSCULAS o entre comillas) en el último frame, ×2, y que coincida con la barra de
      respuesta
    - escasez fuera del CTA (en WN, solo en F1-F2 y en el CTA)
    - palabras por frame, por CTA y por caja (`topes`)
    - cajas y elementos por frame, y un solo resaltado por caja
    - entregable visible en los últimos 3 frames
    - `[corchetes]` sin verificar
    - `compliance` (términos prohibidos, regex, ¿ ¡)
    - gates y variante B
  - **Calendario**:
    - 1 accionable por día
    - no hay CTA en días seguidos fuera de WN
    - descanso de las keywords de recurso
    - `tope_accionables` por semana
    - mezcla semanal contra `mix_objetivo` (en semanas completas)
    - días sin nada para responder
    - keywords sin fila en la tabla

  Sale con código 1 si hay errores. Los flags `--max-palabras`, `--max-cta`, `--max-caja`, `--duros`, `--prohibir` y
  `--sin-signos` pisan al JSON.
- `--png` saca una captura con Playwright y Chrome, y avisa si algún teléfono quedó con contenido cortado (hay que
  partir el frame). Leer la captura con Read antes de entregar.

## DESHIDRATAR
- Perfil → `historias/perfil-marca.md`
- Calendario → `historias/calendario/AAAA-MM.md` + `.json` + `.html` (o `AAAA-MM-DD-semana.*`)
- Secuencia → `historias/secuencias/AAAA-MM-DD-TIPO-KEYWORD.md` + `.json` + `.html` (sin keyword:
  `AAAA-MM-DD-TIPO-tema-corto`)
- Registro → `historias/registro.md` (una fila por accionable y lectura semanal con la semana ISO; dato que no se
  tiene = `s/d`, no se estima)
- Revisión → `historias/revisiones/AAAA-MM-DD-revision-TEMA.md` + `.json` + `.html`
- Si el proyecto ya usa `contenido/historias/`, escribir ahí, respetando lo que exista.
- Última línea en el chat, estado en una línea, p. ej.: `Octubre listo · modo estándar · HR 10 · CTA 7 · WN 26→31 ·
  faltan 2 flows (CLON, INFO) · historias/calendario/2026-10.html`

## Antes de entregar
**Calendario**
- [ ] Se fijaron primero las ventanas y eventos. Hay WN solo si hay urgencia real, con fecha.
- [ ] La mezcla semanal está dentro del modo. Máximo 1 accionable por día. No hay CTAs seguidos fuera de WN.
- [ ] Cada keyword de recurso (HR) tiene 7+ días de descanso y un recurso detrás. El flow figura como ok, falta,
      probar o a-mano. El tope de accionables de la marca se respeta.
- [ ] Todos los días tienen algo para responder.
- [ ] Modo estándar o conservador: encuesta de ángulos temprano y presentación al arranque. Modo push: el arco WN
      completo, con 1 HR o encuesta intercalada y el día de descanso después del cierre.
- [ ] Están los archivos MD, JSON y HTML, más la lista de lo que hay que preparar.

**Secuencia**
- [ ] **Test del hilo**: leyendo solo la primera caja de cada frame, en orden, suena a una historia contada de corrido
      (no a una lista de titulares). Hay `hilo` y cada frame desde el 2 tiene su `puente`.
- [ ] F1 frena el scroll en mute: cara actuada o absurdo con dirección; el dato, si lo hay, está fuera de lo normal
      para el avatar. Cada frame intermedio empuja (al menos un "..." cortado y una escalada).
- [ ] Hay un concepto con nombre propio (HR y CTA) y un recurso ABISMAL (nombre, volumen, ancla y bonus si es
      chico).
- [ ] Los números son crudos y cierran (test del escéptico). Las capturas llevan el texto literal. Si hay permiso,
      se nombra a la gente.
- [ ] El CTA va en una caja con una sola oferta; la pd no pide datos. Hay un remate seco en la voz de la marca.
- [ ] Hay como mucho 1 emoji cada 2 cajas, 1 puteada como máximo (y con sentido), sin muletillas repetidas y el
      tope de largo por tipo. El F1 rota de tipo (`f1_tipo`) respecto de las últimas secuencias de la marca.
- [ ] El resultado está separado de la actividad. Si el cómo del cliente se muestra, hay permiso para ese detalle
      y el rubro está chequeado.
- [ ] Juez adversarial: 3 debilidades primero, topes aplicados, `autoeval.subiria` ≥ 9 (o el tope marcado con el
      insumo que falta).
- [ ] Hay una idea por frame y se respeta el tope de palabras. El texto no tapa la cara.
- [ ] La prueba es real (captura o perfil con números), con su fallback. No hay nada inventado.
- [ ] El entregable está a la vista. La keyword aparece solo al final, ×2, con flecha al cajón. La escasez va solo
      ahí y es real.
- [ ] Se respetan la voz y el compliance del perfil. Pasa el test del desconocido: en 3 segundos se entiende qué
      pasó y por qué importa.
- [ ] Están los gates, las reglas aplicadas y la variante B. El lint no da errores. El HTML está generado (y
      revisado con --png).

**Revisión**
- [ ] Hay veredicto con número si hay métrica, contra el benchmark del tipo correcto.
- [ ] Cada problema dice en qué frame está y qué regla rompe.
- [ ] La versión corregida mantiene lo que funcionaba y está fechada en un día válido.
- [ ] Las preguntas por datos faltantes van al final, sin frenar la entrega.

## Lo que se rompió
*(se agrega abajo con fecha y caso, nunca se borra)*
- **2026-09-25 · prueba con una marca real.** La marca ya tenía `/historias` y un manual con "1 pedido por
  semana". La skill no los veía y proponía 3 pedidos por semana, además de un segundo registro. → HIDRATAR detecta el
  sistema propio y su manual, que mandan; se suma `tope_accionables`.
- **2026-09-25 · prueba WN (coach fitness).**
  - La regla de 7 días de descanso chocaba con el arco WN y con la keyword del programa. → El descanso aplica solo
    a las keywords de recurso.
  - "Sube 3K" chocaba con el compliance "sin precio". → Se dice la fecha, sin monto.
- **2026-09-25 · prueba de revisión.**
  - El lint no distinguía una secuencia rota: tomaba "YO" dentro de "tuyo" y "último" como escasez. → La keyword
    cuenta solo en MAYÚSCULAS o entre comillas, y la escasez con contexto.
  - La causa real era la ráfaga rota (frames subidos con 3 h de diferencia). → Se revisan los horarios de las
    capturas.
