# Métricas: cómo se mide, benchmarks reales y cómo se ajusta

## 1. Qué se mide por secuencia (fila del registro)
`fecha · tipo · estructura · keyword · N° frames · hora · views frame 1 · views frame CTA · views último ·
respuestas (DMs con la keyword) · % respuesta · visitas al perfil · agendas/aplicaciones atribuidas · calidad de
leads (A/B/C/D) · nota`

- **% respuesta = respuestas / views del frame de CTA** (así lo define el método). Anotar también respuestas /
  views del frame 1.
- **Lead = persona que responde la historia** o inicia conversación. Es el único número que cuenta como lead.
- **Decay** = 1 − (views último / views frame 1).
- Views frame 1 / seguidores = alcance de las historias.
- Dónde se ven: Insights de la historia (visualizaciones, respuestas, interacciones, compartidos) + ManyChat/CRM
  (conversaciones con la keyword) + agendas etiquetadas por fuente.

## 2. Benchmarks
| Métrica | Referencia | Fuente |
|---|---|---|
| Respuesta HR | **4-10%** de los que ven el CTA | doc ESTRUCTURA |
| Respuesta CTA directo | **1-3%** | doc ESTRUCTURA |
| Respuesta por tipo (planilla real) | Lead magnet 7-8% · Polls 7-8% · Libre 7-8% · Urgencia 4% / 1% · Libre + urgencia x2 10% | CALENDARIO DE CTA'S (EREX) |
| HR que explotó (Cubria) | 777 respuestas, **~4,7-5%** sobre ~16k views | stats Recurso/ |
| HR más flojo (Cubria) | 218 respuestas, ~1,3-1,4% | stats Recurso/ |
| CTA que explotó (Cubria) | 112 respuestas / 7.281 views = **1,54%** · 88,6% seguidores | stats CTA/ |
| "Qué hago" (Cubria) | 140 respuestas / 8.548 = **1,64%** (2,06% del alcance) · 80,8% seguidores | stats Qué hago_/ |
| WN día 1 (Cubria) | 49 respuestas / 8.013 = **0,61%**; otro día 19 / 9.986 = 0,19% | stats why now 5-6 |
| Respuestas por accionable (cuenta de ~400k) | **200-500 por CTA o HR**; story replies reales: 499, 386, 178, 176, 156, 155, 69 · ~4.500 conversaciones/mes entre reels e historias | Loom "Inbound infinito" (Cubria) |
| Views historia / seguidores | 9% flojo · **15% sano** (cuenta ~3k) | calendario armado para un cliente |
| Decay frame 1 → 5 | **25-30%** sano (ej. 3.159 → 2.200) | Nik |
| Caída de un solo frame | ≥15-20% vs el promedio = ahí está el problema | manual / Nick |
| Completion 7-9 frames | >65% bueno · 71,9% "muy alto" | Nick |
| Leads por 1.000 seguidores | 30-40 reales | Max |
| Lead → agenda | ~3% | SYK |
| Leads para 100k/mes | ~8.000/mes (ticket ~2k) | SYK |
| Ventas desde historias | 85% (SYK); agendas de Cubria por respuestas a historias/comentarios 65% | consultorías |
| Umbral para armar un flow | >20 respuestas esperadas; si no, a mano | Alex / manual |
| Q&A viable | >500 viewers activos | Nick |

**Lectura:** un WN tiene tasa de respuesta baja pero lo contesta gente que compra; un HR tiene tasa alta pero
calidad mixta. Siempre medir **cantidad y calidad**.

## 3. Árbol de diagnóstico (qué cambiar cuando algo no rinde)
```
Views del frame 1 bajas (<10-15% de seguidores)
  → el hook gancho no interesa · cambiar por uno ganador (test §4) · publicar en hora de más actividad
  → pocas historias los días anteriores (la fila se enfría): mantener constancia diaria
Decay alto (>30% en 5) o un frame se lleva ≥15%
  → ese frame: texto largo, idea prescindible, visual estático, sin flecha que empuje · partir o recortar
Muchas views en el CTA pero % respuesta bajo el benchmark
  → HR: el recurso no es "abismal" (engordar: nombre, volumen, que se vea) o no resuelve un dolor del avatar
  → CTA: faltó prueba/FOMO antes o el pedido es grande (bajar a doc de entregables / "para los curiosos")
  → keyword confusa, flecha ausente, o escasez poco creíble
Respuestas altas pero leads de baja calidad
  → el recurso atrae al avatar equivocado · filtrar (pd: "solo si ya…", filtro inverso) · ajustar ángulo
Frames subidos con horas de diferencia (ráfaga rota: revisar la hora de cada captura)
  → casi todos ven el CTA suelto, sin la prueba de antes · subir la secuencia en 10-20 min; si el gancho va antes,
    que igual empuje ("mirá la próxima ➡️")
Cupos "a los primeros N" con muchas respuestas
  → el que llega tarde lo da por lleno y no responde · decir cuántos quedan o "elijo entre los que respondan"
La oferta entera en un solo frame (prueba + pedido + venta avisada)
  → partir: problema → prueba/entregable a la vista → pedido único al final
Respuestas que no se convierten en conversaciones
  → flow roto o lento (probar con DM de test) · setter no sigue · el bot debe calificar (tipo de negocio)
Nadie responde encuestas
  → opciones que no le hablan al avatar · pregunta abstracta · usar rangos o dolores concretos del avatar
```

## 4. Test del hook gancho (cómo encontrar el ganador)
1. En horario de alta actividad (usualmente **12-16 h**), publicar **un hook gancho distinto cada 30 minutos**
   (3-4 en total).
2. El que más views saca = tópico que le interesa a la audiencia → **se repite** en las siguientes secuencias.
3. Método alternativo: Insights → contenido → historias → **últimos 90 días** → ordenar por visualizaciones → los
   temas de las historias con más views son los ganadores.
4. Guardar el banco de 5-10 ganchos ganadores en el perfil (Cubria: "de 5 a 10 hooks que sepan que funcionan
   siempre. Así dejan de inventar todo el tiempo.").

## 5. Ángulos ganadores (qué tema va en las historias de conversión)
- **Jerarquía** para declarar un ángulo ganador (SYK): **clientes que compraron > agendas calificadas > leads
  calificados > leads > views**. Views es lo último que se mira.
- **Último contacto (UC)**: el último contenido que vio o respondió cada cliente antes de agendar/comprar dice qué
  poner en las historias. El primer contacto (PC) dice a qué correr ads.
- Reordenar la matriz de ángulos **cada mes** con los cierres de los últimos 60-90 días.
- La encuesta de ángulos de la semana es el test barato: el ángulo más votado alimenta el HR siguiente.

## 6. Cadencia de revisión
- **Al día siguiente** de cada accionable: cargar la fila del registro (views, respuestas, %).
- **Semanal** (antes de armar la próxima semana): comparar contra benchmark por tipo, detectar el frame que cae,
  actualizar hook ganchos y keywords usadas en el perfil.
- **Mensual**: ángulos por UC, qué estructura rindió mejor, si el modo (conservador/estándar/push) sigue siendo
  el correcto. Cambios de grilla con ≥4 semanas de datos. No juzgar por ventas de 24-48 h.
