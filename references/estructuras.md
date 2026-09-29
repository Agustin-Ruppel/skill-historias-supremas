# Estructuras de secuencia, frame por frame

> Catálogo sacado de ~120 secuencias reales. Fuentes: @ramiro.cubria, sus clientes y cuentas que usan su
> método (cristiansocial, mateomaffia, fiarivera, juanpicrea, matelezama, agustinbadt, nahue.urso), el doc
> ESTRUCTURA (Alex Carrera), Nick Setting y Max Inhouse.
> Cada estructura tiene un código. Buscá el ejemplo real con `grep -n "<código o tema>" references/corpus/*.md`.
> **Se modela la forma, nunca se copia el copy ni el tema.**

## Dónde está cada estructura
| Tipo del día | Archivo |
|---|---|
| HR | `estructuras/hr.md` |
| CTA | `estructuras/cta.md` |
| WN | `estructuras/wn.md` (incluye microlanzamiento) |
| POLL · AWARE · PRUEBA · LIBRE · PRESENTACION · TEASER | `estructuras/nutricion.md` |

Cargá SOLO el archivo del tipo del día (+ este índice).

---

## El hilo conductor (obligatorio en TODA secuencia, antes que la estructura)

Una secuencia no es una lista de datos buenos: es **UNA historia o UN argumento** que se cuenta en N frames. Si
cada frame se puede mover de lugar sin que se note, no hay hilo y el que mira se va en el 2.

**1 · La línea.** Antes de escribir un solo frame se escribe la secuencia en UNA frase:
`[a quién] + [el problema o la afirmación] + [la prueba] + [lo que se pide]`.
Ej: *"al infoproductor que vende por llamada se le escapa plata que nadie mide; te lo muestro con un cliente y si
te pasa, preguntame"*. Si no entra en una frase, son dos secuencias.

**2 · Un protagonista o una afirmación.** Toda la secuencia sigue a UN caso (el mismo cliente de principio a fin,
como el caso Mario López de A-10) o prueba UNA afirmación con varios ejemplos ("todos estos con menos de 2mil
seguidores", PR-STACK). Si entra un segundo caso, tiene que ser **la continuación del mismo argumento**
("eso fue medir; esto es arreglarlo"), nunca "otro cliente…" suelto.

**3 · Cada frame contesta la pregunta que dejó abierta el anterior.** Es la cadena de Cubria:
| Frame que termina con… | …el siguiente arranca con |
|---|---|
| una pregunta ("Cómo encontrás tus ángulos ganadores?") | la respuesta ("1. Hacés una trazabilidad inversa…") |
| una frase cortada ("es porque no tenés…") | el remate ("Ángulos de Comunicación Ganadores") |
| un dato que sorprende ("8 de cada 29 nunca atendían") | el porqué o el quién ("y nadie lo sabía… lo vio el sistema") |
| una promesa ("te muestro cómo 👉") | lo prometido |
| el problema | la causa o la solución ("el problema no son los reels. es…") |
| la solución | la prueba de que funciona |
| la prueba | el pedido ("querés lo mismo? respondé…") |
Conectores que atan: **pero · por eso · entonces · ¿cómo? · y el problema era… · resultado:** (regla "pero / por
eso": entre frames va una consecuencia o un giro, nunca "y además"). Continuidad verbal ("nadie me avisó…" → "de
lo que sí te vengo avisando…") y el mismo número que se va desarrollando también atan.

**4 · El gancho también se ata.** El hook gancho puede no tener que ver con el negocio, pero su último bloque
tiende el puente: la pd ("pd: del mismo sabor de los prospectos que te llegan 🤣"), el giro ("chiste aparte… mirá
la próxima ➡️") o la continuidad verbal.

**5 · Test del hilo (se hace siempre antes de entregar):** leé SOLO la primera caja de cada frame, en orden. Tiene
que sonar a una historia contada de corrido. Si suena a lista de titulares, se reescribe.

**Anti-patrones:** abrir cada frame con un tema nuevo · "otro cliente…", "además…", "por otro lado…" · presentarse
("soy X") en el medio sin que venga del frame anterior · mezclar dos problemas distintos · un CTA que pide algo que
la secuencia no preparó.

En el JSON: `hilo` (la línea) y, en cada frame desde el 2, `puente` (qué pregunta del anterior contesta). El lint
avisa si faltan y el HTML los muestra, para que el hilo se pueda revisar de un vistazo.

---

## Árbol de decisión (con el tipo del día y los insumos que hay)

```
¿Qué tipo toca hoy (del calendario)?
├─ HR ─┬─ ¿hay objeción repetida esta semana?        → HR-OBJ (A) · variante burla HR-MOCK
│      ├─ ¿llegó una pregunta a la caja/DM?          → HR-CAJA (I)
│      ├─ ¿resultado propio con captura?            → HR-RES (C) · o HR-CLASICO si hay hook gancho
│      ├─ ¿caso de cliente fresco con permiso?      → HR-CASO · o HR-CLASICO (gancho → resultado → vehículo → CTA)
│      ├─ ¿recurso "de clientes" / clase interna?   → HR-LEAK (1-2 frames) · HR-REVEAL (activo con nombre propio)
│      ├─ ¿varios recursos del mismo tema?          → HR-STACK (Solución N.1/N.2/N.3 + BONUS)
│      ├─ ¿el problema se puede cuantificar?        → HR-COSTO ("ESTÁS PERDIENDO 4hs POR DÍA")
│      ├─ ¿concepto propio para nombrar el dolor?   → HR-DIAG ("AUDIENCIA LATENTE")
│      ├─ ¿hito (N seguidores, aniversario)?        → HR-HITO
│      ├─ ¿poco tiempo para producir?               → HR-TEASE (2 frames) · HR-DISPONIBLE (1 frame)
│      ├─ ¿momento del año / arranque de mes?       → HR-ESTACIONAL (M)
│      ├─ ¿encuesta hoy y reveal a la tarde?        → HR-ENCUESTA (repartida en el día)
│      └─ ¿el regalo es tu servicio?                → HR-AUDIT (auditoría por chat)
├─ CTA ┬─ ¿semana cargada de clientes / calls?      → CTA-CALLS ("CTA que explotó")
│      ├─ ¿4-5 wins frescos?                        → CTA-STACK ("para los curiosos")
│      ├─ ¿un caso fuerte con antes/después?        → CTA-CASO (B) · CTA-ANTESDESP (doble caso)
│      ├─ ¿querés explicar el programa?             → CTA-WALK (D) · CTA-FUTURO ("qué va a pasar cuando…")
│      ├─ ¿resultado propio + "cómo lo replicás"?   → CTA-REPLICA (C+D)
│      ├─ ¿audiencia con dudas de precio/garantía?  → CTA-CURIOSOS (doc de entregables)
│      ├─ ¿"por qué vos" es la objeción?            → CTA-PORQUE ("por qué conmigo")
│      ├─ ¿mensajes de alumnos + promedio?          → CTA-PROMEDIO (costo de inacción)
│      ├─ ¿la promesa se puede mostrar con cuenta?  → CTA-MATE (calls × % × ticket)
│      ├─ ¿grabás a cámara hoy?                     → CTA-HABLADO (honesto, sin editar)
│      └─ ¿secuencia ganadora de antes?             → CTA-RECICLA (mismo cuerpo, cierre nuevo)
├─ WN ─┬─ primer día de la ventana                  → WN-ANUNCIO
│      ├─ días intermedios                          → WN-CUPOS (bajar cupos) · WN-POSDATA · WN-FLASH (bonus stack)
│      ├─ se agotó y hay reapertura real            → WN-REAPERTURA
│      ├─ último día                                → WN-CIERRE (H) · WN-FIN (cierre narrativo)
│      ├─ semana previa                             → WN-WARMEO · WN-AUTORIDAD
│      ├─ versión corta                             → WN-PARROQUIAL (3 frames)
│      └─ momento del año                           → WN-ESTACIONAL (M) / microlanzamiento
├─ POLL → POLL-ANGULOS · POLL-SEGMENTA · POLL-QUIZ · QA-AMA · QA-CAJA · POLL-CTA (2 opciones que son sí)
├─ AWARE → AW-CLIENTES · AW-SEMANA · AW-POV-MES · AW-PRODUCTO · AW-SISTEMA · AW-RAZONES · AW-PALANCAS · AW-PIZARRON
├─ PRUEBA → PR-STACK (F) · PR-RECAP · PR-SISTEMA (sin casos: el sistema propio) · PR-NICK (Client Result Stacking)
├─ LIBRE → LB-VLOG · LB-GANCHOS (test) · LB-OPINION · LB-NOSTRUCT
├─ PRESENTACION → PRE-QUEHAGO
└─ TEASER → TS-ENCUESTA (G) · TS-EVENTO · TS-LOOP
```
Si faltan insumos para la estructura ideal (no hay caso, no hay captura), se baja a una que no los necesite: no se
inventa prueba. Sin casos, el activo es **el sistema propio corriendo**.

---

## Piezas sueltas que se insertan en cualquier estructura
- **Frame puente de aire** (guion de referencia): caja blanca sola con un hecho concreto antes del CTA ("cada producto del container del lunes pasó por este filtro."), sin keyword. Respira antes del pedido.
- **Prueba de entrega** post-CTA: captura del DM automático + "llega al instante" / "(le llega automático a TODOS)".
- **pd calificador** en crema después del CTA: "pd: contame en el dm en qué rubro estás" (ordena el DM para el setter).
- **Rótulo pre-digestor** en crema arriba de una captura: "está en el top 3 de preguntas que me hacen 👇".
- **Recordatorio** horas después de un CTA fuerte: mismo frame de CTA con "por si te lo perdiste".
