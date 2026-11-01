# CO2 — Indicadores egocéntricos sobre v0.2.2

Especificación fijada antes de obtener resultados. Fecha: 30 de octubre de 2026. Esta es una capa derivada de indicadores, no una nueva corrección de la base v0.2.2.

## Universo y unidad

Se reutilizan las identidades, documentos, años y eventos corregidos de v0.2.2. Contexto único: investigador i y año t con una publicación resultado recuperada. La red previa G_t incluye únicamente documentos cuyo año bibliográfico aplicado está entre t−3 y t−1, inclusivos; no incluye ningún documento de t ni años posteriores. No se inventa secuencia intranual. Las observaciones sin año se conservan en la vinculación a resultados con indicadores faltantes.

Se calculan los indicadores una vez por contexto y se vinculan después mediante una unión muchos-a-uno con investigador–publicación. Elegibilidad analítica: al menos una publicación resultado que cumple F6 v0.2.2. También se entregan todos los contextos observados; no se filtra por temática, cambio de firma o valor del indicador. Se presenta separadamente F6 con al menos dos colaboradores, sin borrar los casos de cero o uno.

## Red y pesos

Red no dirigida, sin autorrelaciones. w_uv es el número de publicaciones distintas compartidas por u y v en la ventana; una publicación deduplicada aporta una vez a cada pareja de su equipo recuperado. Los equipos originales se preservan. Un peso representa frecuencia de coautoría recuperada, no tiempo, esfuerzo, confianza o inversión real.

A_i = vecinos de i; n_i = |A_i|. M_i = número de parejas distintas entre A_i con al menos una coautoría previa. Densidad d_i = 2M_i/[n_i(n_i−1)], solo si n_i≥2. Con cero o un colaborador la densidad es NA, con motivo explícito; no se sustituye por cero ni se clasifica como intermediación. Se conservan por separado publicaciones focales con al menos un coautor identificado y publicaciones reconocibles como de coautoría aunque solo se haya recuperado un firmante.

## Constraint ponderado de Burt

s_u = Σ_{k∈N(u)} w_uk; p_uv = w_uv/s_u, con p_uv=0 cuando no existe vínculo. En red no dirigida, usar pesos mutuos (w_uv+w_vu) produce la misma proporción. Se usa la fuerza del alter sobre TODOS sus vecinos observados en G_t, incluidos los que están fuera del ego inducido. No se renormaliza cada alter solo dentro del conjunto A_i.

C_i = Σ_{j∈A_i} [p_ij + Σ_{q∈A_i} p_iq p_qj]².

C_i es NA si n_i=0. Con n_i=1, C_i=1. No se recorta artificialmente a [0,1]: puede superar 1. Valores altos indican mayor restricción/redundancia en la métrica; NO mayor intermediación. Los casos de n_i<2 se identifican y no se interpretan automáticamente como posiciones intermediarias.

## Tamaño efectivo ponderado

m_jq = w_jq / max_{k∈N(j)} w_jk, con m_jq=0 si no hay vínculo.

E_i = Σ_{j∈A_i} [1 − Σ_{q∈A_i} p_iq m_jq].

La normalización de m utiliza también todos los vínculos observados de j en G_t. E_i es NA para aislados y 1 con un único colaborador. La eficiencia E_i/n_i es NA cuando n_i=0. Se entrega adicionalmente tamaño efectivo binario E_i(bin)=n_i−2M_i/n_i, que permite comprobar la relación con la densidad. Para n_i≥2, E_i(bin)=n_i−d_i(n_i−1): su asociación con densidad no es un hallazgo independiente. No se identifica un tamaño efectivo alto con liderazgo o resultados superiores.

## Repetición, separada del cierre

S_i=Σ_j w_ij = número de eventos focal–colaborador–publicación. R_i=Σ_j max(w_ij−1,0)=S_i−n_i. Proporción de repetición de eventos: R_i/S_i, NA si S_i=0. Número de colaboradores repetidos: cuenta de j con w_ij≥2; proporción sobre n_i, NA si n_i=0. Se cuentan también colaboradores con coautoría en al menos dos años distintos. Varias publicaciones de la misma pareja en un solo año constituyen multiplicidad documental; no se afirma cuál fue primera dentro de ese año. Estas medidas no utilizan vínculos alter–alter y no son medidas de cierre.

## Procedencia del cierre proyectado

Cada evento entre alter se marca según el documento incluya o no al focal. Las parejas se particionan en: solo documentos con focal, solo documentos sin focal y ambos tipos. Se distinguen número de parejas y número de eventos pareja–documento. La proporción de parejas con respaldo de algún documento con focal usa M_i como denominador y es NA cuando M_i=0.

Se entrega densidad respaldada por publicaciones sin focal: parejas de las categorías solo-sin y ambas divididas por n_i(n_i−1)/2. Es una descripción documental, no una red causalmente independiente. La proyección de un único equipo multiautor ya genera un clique: densidad elevada no demuestra confianza, coordinación ni un mecanismo social autónomo.

## Incertidumbre y linaje

Se registran identidades NAME/NAMEEMAIL, variantes y conflictos nominales/de orden heredados, conflictos documentales de identidad conocidos, fechas no contrastadas o discrepantes y equipos parciales o de tamaño incierto. Desconocido/no contrastado no significa erróneo. La validación del piloto se limita a sus pares focal–documento y reparaciones locales. Los conflictos de orden no se equiparan automáticamente a errores de identidad.

Se conservan dos alcances de soporte documental: (a) documentos que generan vínculos focal–alter o alter–alter del ego; (b) además, documentos incidentes a los alter que intervienen en los denominadores de constraint y tamaño efectivo, aunque conecten con terceros fuera del ego. Ambos soportes están restringidos a la misma ventana. Las marcas de calidad describen evidencia disponible en v0.2.2; no acreditan historias completas.

## Diagnóstico descriptivo

Distribuciones y faltantes en tres universos: todos los contextos, contextos F6 y F6 con n_i≥2. Las correlaciones Pearson y Spearman se calculan por pares completos de contextos únicos, con n y número de investigadores explícitos, sin p-valores; Spearman usa rangos medios calculados dentro de cada par. Se requieren al menos tres pares y varianza positiva. No se calculan correlaciones sobre la tabla duplicada por publicaciones.

La variación dentro del investigador utiliza contextos F6 y, separadamente, F6 con n_i≥2. Se cuentan cero, uno, dos y tres o más contextos por investigador. Rango, desviación estándar muestral y diferencia último–primer contexto se dejan NA con menos de dos valores definidos; no se confunde observación única con constancia. Tolerancia de variación numérica: 1e−10. Los años consecutivos pueden compartir dos años de antecedentes; no son muestras independientes.

La tabla de firma actual por antecedentes conserva primera/no primera y las tres categorías previas, incluida mixta. Se entrega por publicaciones y, aparte, por contexto, permitiendo que un mismo año tenga ambos tipos de firma actual. No se estiman modelos ni efectos causales.

## Fuentes de las definiciones

Burt, R. S. (2004). Structural holes and good ideas. American Journal of Sociology, 110(2), 349–399. https://doi.org/10.1086/421787

NetworkX Developers. (2026). Constraint; local_constraint; effective_size [Documentación técnica, versión consultada 3.7]. https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.structuralholes.constraint.html ; https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.structuralholes.local_constraint.html ; https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.structuralholes.effective_size.html

La fórmula binaria se atribuye a Borgatti en la documentación técnica. No se afirma haber inspeccionado el texto completo de su artículo original, cuya página no fue recuperable en esta consulta. Las fórmulas ponderadas y sus normalizaciones se documentan explícitamente arriba para que su implementación no dependa de una versión de biblioteca.
