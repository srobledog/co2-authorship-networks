# CO2 — Auditoría del tratamiento de la dependencia e inferencia

**Diagnóstico v0.1 · 31 de octubre de 2026.** Muestra analítica v0.1 / base v0.2.2 / modelos exploratorios v0.1. Los insumos, entregables previos, manuscrito y H1/H2 permanecen intactos.

## Recomendación para coordinación

**Retirar los percentiles del remuestreo cruzado de v0.1 como fundamento para evaluar H1/H2.** Conservarlos archivados como diagnóstico del procedimiento. Las estimaciones puntuales de la primera ronda no cambian, pero ese remuestreo no aporta una base suficiente para sus conclusiones inferenciales. Tampoco sustituirlo automáticamente por uno de los métodos comparados aquí.

El desplazamiento de la heterogeneidad se reproduce al ponderar únicamente las publicaciones dentro de la integral de cada investigador, sin remuestrear investigadores. Los remuestreos de bloques completos y la simulación del propio modelo de trabajo presentan centros mucho más próximos al ajuste original. Es evidencia específica de que el procedimiento de ponderación interna produce la anomalía en esta implementación y estos datos; no es una prueba de invalidez universal del pigeonhole bootstrap ni una validación de las alternativas.

Esta auditoría examina **solo M0**, para no escoger un tratamiento inferencial según el resultado de H1 o H2. No se estimaron nuevos modelos de esas hipótesis ni se cambiaron sus especificaciones.

## Diseño registrado y límites

Se utilizaron las 1.079 observaciones principales hasta 2025: 292 investigadores, 717 contextos y 765 publicaciones. Los controles, antecedentes y ventana [t−3,t−1] no cambian. Se realizaron 199 réplicas por diagnóstico, con semillas documentadas en `00_PROTOCOL_BEFORE_DIAGNOSTICS.md`, y se reutilizaron las 399 réplicas cruzadas previas de M0. Los intervalos de la tabla son **percentiles descriptivos de distribuciones de diagnóstico**, no IC con cobertura demostrada.

Los cuatro diagnósticos nuevos separan: multiplicidades externas de investigadores; multiplicidades internas de publicaciones; remuestreo externo de componentes completos de investigadores que comparten publicaciones resultado; y simulación paramétrica con nuevos interceptos Normales y resultados Bernoulli independientes condicionalmente. Esta última es una referencia deliberadamente limitada al modelo de trabajo: no simula el proceso real de asignación de primera autoría. No es un estudio de cobertura ni permite estimar sesgo o error tipo I en CO2.

| Procedimiento | Utilizables / intentadas | Mediana σ | Percentiles σ | Mediana / σ original | Réplicas con σ en límite inferior |
| --- | --- | --- | --- | --- | --- |
| Solo investigadores | 199 / 199 | 0.507 | 0.001–0.742 | 0.96 | 8 |
| Solo publicaciones (peso interno) | 199 / 199 | 1.742 | 1.355–2.175 | 3.29 | 0 |
| Componentes completos de resultados | 199 / 199 | 0.483 | 0.001–0.884 | 0.91 | 31 |
| Simulación paramétrica de trabajo | 199 / 199 | 0.507 | 0.119–0.794 | 0.96 | 3 |
| Cruzado previo (v0.1) | 399 / 399 | 1.744 | 1.114–2.572 | 3.29 | 0 |

El ajuste original estima σ = **0.530**. Los límites inferiores equivalen a σ≈exp(−7)=0,000912, aproximación numérica a varianza cero; se conservan y no se tratan como réplicas fallidas.

![Comparación de procedimientos](figures/diagnostico_remuestreo_sigma.png)

## Qué identifica la comparación

En el procedimiento cruzado original se maximiza una suma ponderada de log-verosimilitudes integradas, con pesos de publicación dentro del producto de Bernoulli. Duplicar internamente las contribuciones de una misma respuesta cambia la composición y la precisión interna del historial de cada investigador. La integración es no lineal: ponderar Bernoulli dentro de la integral no equivale a ponderar un bloque integrado completo fuera de ella.

El diagnóstico de solo publicaciones conserva a todos los investigadores sin multiplicidad externa y reproduce el fuerte desplazamiento de σ. Por contraste, el diagnóstico de solo investigadores remuestrea historiales completos y no muestra ese desplazamiento de centro. Esta separación de operaciones localiza la anomalía; no demuestra cobertura nominal de los coeficientes fijos. Las diferencias de σ por sí solas tampoco prueban que todos los percentiles de β tengan un sesgo de signo o magnitud conocidos.

El alcance teórico del pigeonhole bootstrap y del remuestreo de arreglos cruzados no autoriza trasladar sin validación una garantía de cobertura a esta verosimilitud mixta no lineal (Owen, 2007; Owen & Eckles, 2012). Austin y Leckie (2020) comparan procedimientos para modelos logísticos multinivel; sirven como referencia para distinguir esquemas de remuestreo, no como validación de esta red cruzada.

## Estructura observada de dependencia

Los investigadores se conectaron si compartían una publicación **resultado** dentro de la muestra. Cada componente conserva íntegramente los bloques de investigador y todas las publicaciones resultado compartidas observadas. Estos componentes son agrupaciones de la muestra analítica, no los componentes de la red bibliométrica ampliada original.

| Diagnóstico | Valor |
| --- | --- |
| Componentes observados | 141 |
| Componentes de un solo investigador | 101 |
| Observaciones del componente mayor | 339 / 1.079 (31.4%) |
| Observaciones en los dos mayores | 43.5% |
| Inverso de Herfindahl por conteo de observaciones | 8.01 |

El inverso de Herfindahl es 1/Σₖ(nₖ/N)². Es un resumen de concentración por tamaño, **no un número de grados de libertad ni una estimación de unidades independientes para todos los coeficientes**. Un componente aporta casi un tercio de las filas; su omisión o duplicación puede dominar el remuestreo. Aunque el remuestreo por componentes conserva la estructura observada y su mediana de σ es próxima al original, eso no establece su calibración inferencial.

Los componentes tampoco garantizan independencia real: puede haber coautores omitidos, conexiones previas u otros factores comunes. A su vez, compartir covariables construidas con publicaciones previas no demuestra por sí solo dependencia residual de los resultados condicionados a esas covariables. Conviene distinguir dependencia de resultados, incertidumbre compartida de medición y mera superposición de predictores.

## Restricción de una única primera firma

En las 765 publicaciones observadas no aparece más de una primera firma por artículo. La primera firma está representada en 352 y ausente del subconjunto analítico en **413**. Esta ausencia no es un dato perdido de la posición de los investigadores incluidos: el primer autor puede existir fuera de la muestra elegible. Solo 66 publicaciones tienen tantas filas elegibles como autores en la evidencia máxima heredada; esto no acredita que todos sus equipos estén documentalmente validados.

Un modelo conjunto de elección de primera firma requeriría otro diseño y otro estimando. Entre los documentos actuales, 179 publicaciones, que aportan 418 observaciones, tienen al menos dos investigadores elegibles y su primera firma incluida. Son un diagnóstico de soporte potencial; **no se seleccionaron para un modelo**. Restringirse automáticamente a ellas excluiría gran parte de la muestra y cambiaría el alcance.

La simulación paramétrica del modelo de trabajo generó más de una primera firma en una mediana de **33 publicaciones por réplica** (rango 20–48); ocurrió en 199/199 réplicas. Esto expone una incompatibilidad de una interpretación conjunta del modelo Bernoulli independiente. El esquema solo se usa como control interno del comportamiento de σ, nunca como simulación validada del mecanismo real de autoría. Un intercepto positivo compartido por publicación no impondría la restricción de una única primera firma.

## Decisión metodológica recomendada

1. Mantener las estimaciones puntuales y probabilidades de v0.1 como resultados exploratorios del modelo de trabajo, con sus límites de cobertura documental y sin lenguaje causal o de liderazgo demostrado.
2. No utilizar los percentiles cruzados previos para sostener o descartar H1/H2. Mantener los intervalos de Hessiana únicamente con la advertencia de que no corrigen publicaciones compartidas.
3. No escoger un bootstrap porque conserve mejor una dirección esperada o produzca intervalos más estrechos. Los diagnósticos de investigador y componentes son referencias metodológicas; ninguno queda adoptado como solución definitiva.
4. Antes de una nueva ronda inferencial, fijar el estimando: asociación individual marginal (que permitiría evaluar un modelo marginal y una covarianza por investigador/publicación) o asignación conjunta de primera firma por artículo (que exige representar los conjuntos de alternativas y los autores fuera del subconjunto). Son diseños distintos, no reparaciones intercambiables del mismo OR.

Mi recomendación inmediata es conservar la ronda actual como **exploratoria y descriptiva**. Si la prioridad posterior sigue siendo la asociación individual de H1/H2 sobre toda la muestra, el candidato a evaluar es una especificación marginal con tratamiento explícito de ambos agrupamientos; deberá registrarse y validarse como un estimando diferente del OR condicional del GLMM. No se ha estimado aquí ni se garantiza que una covarianza agrupada repare una media mal especificada. No se amplía ahora el estudio hacia nuevos indicadores ni se recuperan nuevos documentos.

## Verificación, archivos y reproducción

Los 796 ajustes diagnósticos nuevos conservan su respuesta, semilla, parámetros y diagnóstico de convergencia en `output/diagnostic_raw.jsonl`; no se reemplazaron réplicas según resultados favorables. Se verificó cuadratura adaptativa de 80 frente a 120 nodos y el gradiente proyectado. Las soluciones en límite inferior se registran separadamente. El paquete incluye datos de entrada copiados sin cambios, estimaciones y remuestreo cruzado previos, protocolo anterior a estos cálculos, estructura por artículo/componente, comparaciones, figura y código autónomo.

- `resampling_comparison.csv`: centros, percentiles y soluciones en el límite.
- `M0_fixed_coefficient_centers.csv`: comparación diagnóstica de todos los β de M0, sin nuevos contrastes H1/H2.
- `outcome_components.csv` y `row_component_membership.csv`: componentes y pertenencia por fila.
- `publication_representation.csv`: presencia de primera firma y representación del equipo.
- `parametric_incompatibility.json`: violaciones de unicidad en la simulación del modelo de trabajo.
- `numerical_diagnostics.csv`: convergencia y comprobación de integración por réplica.

## Referencias

Austin, P. C., & Leckie, G. (2020). Bootstrapped inference for variance parameters, measures of heterogeneity and random effects in multilevel logistic regression models. *Journal of Statistical Computation and Simulation, 90*(17), 3175–3199. https://doi.org/10.1080/00949655.2020.1797738

Owen, A. B. (2007). The pigeonhole bootstrap. *The Annals of Applied Statistics, 1*(2), 386–411. https://doi.org/10.1214/07-AOAS122

Owen, A. B., & Eckles, D. (2012). Bootstrapping data arrays of arbitrary order. *The Annals of Applied Statistics, 6*(3), 895–927. https://doi.org/10.1214/12-AOAS547
