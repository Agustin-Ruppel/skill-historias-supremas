# historias-ig

**Una skill de Claude Code que te dice qué historias de Instagram subir cada día y te las escribe frame por frame.**
La armé estudiando cómo hacen historias las cuentas que más venden con ellas.

Hecha por **Agustín Ruppel** · [@agustin.ruppel](https://instagram.com/agustin.ruppel)

![Secuencia de ejemplo](docs/secuencia.png)

---

## Qué hace

- **Calendario del mes o de la semana.** Te dice qué tipo de historia va cada día: hand raiser, CTA, why now,
  encuesta, awareness, prueba social o libre. También fija con qué keyword, qué recurso y en qué ventana de
  urgencia.
- **La secuencia del día, frame por frame.** El texto de cada caja (negra, blanca, crema o amarilla), el visual,
  cómo actuarlo, el sticker, la música, el CTA y lo que tenés que tener listo antes de publicar.
- **Un juez adentro.** Antes de entregarte nada, la secuencia se puntúa contra el estándar de las historias que
  realmente venden. Si no llega a 9/10, se reescribe.
- **Registro.** Le pasás views y respuestas y te dice si estás arriba o abajo del benchmark de ese tipo de
  historia, y qué cambiar la semana siguiente.
- **Revisión.** Le pasás capturas de una secuencia que ya subiste y te dice qué rompió y te la devuelve
  corregida.

Todo sale en `.md` (para copiar a Instagram) y en `.html` (la placa visual, para vos o tu equipo).

![Calendario de ejemplo](docs/calendario.png)

## De dónde sale

- **~120 secuencias reales transcriptas frame por frame**, de cuentas que venden con
  historias. Están en `references/corpus/` y la skill las usa como ejemplos cada vez que escribe.
- **Un método de calendario probado**: cuántos hand raisers, CTAs y why now por semana, y cuándo va cada uno.
- **Stats reales** de historias que explotaron: tasa de respuesta por tipo, qué es bueno y qué es flojo.
- **~60 estructuras con nombre** (HR, CTA, WN, encuestas, awareness), cada una con su molde y su ejemplo real.
- **Un loop de calidad**: la skill generó secuencias, un juez muy exigente las destrozó, y cada error quedó
  escrito como regla dentro de la skill.

## Instalación

```bash
git clone https://github.com/Agustin-Ruppel/skill-historias-supremas ~/.claude/skills/historias-ig
```

Necesitás **Claude Code** y **python3**. Si también querés que te saque la captura PNG de cada placa:

```bash
pip install playwright && playwright install chromium
```

## Cómo se usa

Abrí Claude Code en la carpeta de tu proyecto (o la de tu cliente) y pedile:

- `armame el calendario de historias de octubre`
- `qué historias subo hoy`
- `armá la secuencia del jueves: hand raiser con keyword GUIA`
- `revisá esta secuencia` y le pegás las capturas
- `registrá cómo fue la de ayer: 4.100 views, 38 respuestas`

La primera vez te hace unas preguntas, cada una con una respuesta por defecto: qué vendés, qué recursos tenés,
qué casos podés mostrar y tu tono. Con eso arma tu perfil de marca y no vuelve a preguntar. Sirve para varias
marcas: cada proyecto tiene su perfil.

## Qué hay adentro

```
historias-ig/
├── SKILL.md                    el procedimiento (lo que lee Claude)
├── references/
│   ├── nivel-calidad.md         el estándar de calidad + el juez
│   ├── metodo.md               los 9 tipos de historia y para qué sirve cada uno
│   ├── calendario.md           el motor: qué va cada día, semana y mes
│   ├── estructuras.md          árbol de decisión + estructuras/ (hr · cta · wn · nutrición)
│   ├── copy.md                 banco de hooks, CTAs, escasez, keywords
│   ├── visual.md               cajas, neón, capturas, grabación
│   ├── metricas.md             benchmarks y qué cambiar cuando algo no rinde
│   ├── perfil-marca.md         el onboarding de cada marca
│   ├── plantillas-output.md    los formatos de salida
│   └── corpus/                 las secuencias reales (INDEX.md para buscar)
├── assets/                     plantillas HTML + ejemplos JSON
├── scripts/render.py           arma el HTML y chequea las reglas (lint)
└── examples/                   una secuencia y un calendario de ejemplo
```
