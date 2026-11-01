# CO2 — Revisión acotada del procedimiento de inferencia

**Revisión v0.2 · 31 de octubre de 2026.** Se conservan intactos los ajustes originales, sus datos y la auditoría v0.1. No se amplían predictores ni se reformulan hipótesis.

## Conclusión y alcance

La implementación reproduce el remuestreo cruzado que se había programado: multiplicidades de investigadores fuera de la log-verosimilitud integrada y multiplicidades de publicaciones dentro del producto Bernoulli. Los casos pequeños lo confirman mediante clonación literal de filas e identificadores. **No se identificó un error de programación en la ubicación de esos pesos respecto de ese plan de remuestreo.**

Eso no establece que el plan sea adecuado para aproximar la distribución de los estimadores del GLMM. La ponderación interna cambia el balance entre información de las respuestas y la distribución de un único efecto aleatorio por investigador. El procedimiento no es equivalente a remuestrear historiales completos. La diferencia es inherente al esquema elegido, no una prueba de error de cuadratura ni evidencia sustantiva sobre colaboración.

Se seleccionó, antes de simular resultados, una alternativa que conserva la función de estimación y sus estimaciones puntuales: **covarianza sandwich de los scores agregados por bloques completos de dependencia**. Se evaluó en 1.500 conjuntos sintéticos, incluidos escenarios con una única primera firma por artículo. El candidato no superó todo el criterio de calibración registrado antes de los cálculos, por lo que **no se aplicó a CO2**. No se eligió ni descartó por producir intervalos más estrechos o resultados favorables de H1/H2.

## 1. Qué representa σ

El modelo de trabajo es

\[
Y_{ij}\mid b_i,X_{ij}\sim\mathrm{Bernoulli}(p_{ij}),\qquad
\operatorname{logit}(p_{ij})=X_{ij}^{\top}\beta+b_i,\qquad
b_i\sim N(0,\sigma^2).
\]

σ es la **desviación estándar de la distribución del intercepto aleatorio por investigador**, en escala de log-odds, condicionada a los predictores y a la especificación del modelo. Es un parámetro de heterogeneidad latente y un parámetro nuisance para la inferencia sobre β. No es el error estándar de un coeficiente, la desviación de las posiciones de firma observadas ni una medida de liderazgo.

En el ajuste original M0 de la muestra principal, σ≈0,530. En esta especificación, un cambio de un σ en b equivale a multiplicar las odds condicionales por exp(0,530)≈1,70, manteniendo las covariables. Esta equivalencia describe el modelo, no una comparación causal o una capacidad científica observada. El intercepto se comparte en todas las observaciones de un investigador; no es un efecto distinto por publicación ni por año.

La densidad normal φσ(b) es la distribución de mezcla de los efectos aleatorios, **no un prior bayesiano sobre β o sobre σ**. Los ajustes originales se hicieron por máxima verosimilitud marginal. Bajo la dependencia y cobertura incompletamente modeladas de CO2, σ debe presentarse como parámetro del modelo de trabajo, no como heterogeneidad poblacional validada.

## 2. Dónde entran las multiplicidades

Para un investigador i, sea

\[
L_i(\theta)=\int \phi_\sigma(b)\prod_{j\in\mathcal J_i}f_{ij}(Y_{ij}\mid b;\beta)\,db,
\quad\theta=(\beta,\log\sigma).
\]

El objetivo original es \(\ell(\theta)=\sum_i\log L_i(\theta)\). Es una verosimilitud marginal de trabajo por investigadores, no una distribución conjunta completa de todas las firmas de cada publicación.

En cada réplica anterior se generan, de forma independiente,

\[
(a_1,\ldots,a_I)\sim\mathrm{Multinomial}(I;1/I,\ldots,1/I),\quad
(m_1,\ldots,m_J)\sim\mathrm{Multinomial}(J;1/J,\ldots,1/J).
\]

El programa maximiza

\[
\ell^*(\theta)=\sum_i a_i\log\left\{
\int\phi_\sigma(b)\prod_{j\in\mathcal J_i}
 f_{ij}(Y_{ij}\mid b;\beta)^{m_j}\,db\right\}.
\]

| Elemento | Peso recibido | Interpretación |
| --- | --- | --- |
| Contribución Bernoulli de una observación i–j | mⱼ dentro del producto | Repite o elimina esa respuesta dentro del historial del investigador. |
| Densidad normal dentro de una copia del investigador | Una sola φσ(b); no se eleva a mⱼ | Mantiene un único efecto aleatorio por copia del investigador. |
| Logaritmo de la integral completa del investigador | aᵢ | Repite su contribución marginal integrada; cada copia literal tiene un nuevo identificador de efecto aleatorio. |
| Normalización multinomial | Totales I y J en sus respectivas dimensiones | No impone un total constante de observaciones efectivas en cada réplica. |

Estos pesos son multiplicidades de remuestreo, no pesos de probabilidad inversa de inclusión ni ponderaciones de un diseño probabilístico documentado de recuperación bibliográfica.

Si aᵢ=2, el término es 2 log ∫φσ(b)Fᵢ(b)db: dos copias integradas separadamente. No equivale a log ∫φσ(b)Fᵢ(b)²db, que comparte un solo efecto aleatorio entre las respuestas duplicadas. Tampoco corresponde a elevar arbitrariamente la densidad normal a una potencia para igualar los pesos: eso definiría otra operación y no repararía el procedimiento sin justificar otro diseño.

## 3. Muestreo representado y balance interno

La clonación literal de investigadores y publicaciones reproduce la fórmula ponderada del remuestreo cruzado. Por tanto, se está reproduciendo ese plan explícito de muestreo de arreglos, con las dependencias particulares que induce. Sin embargo, la inferencia pretendida necesita además justificar por qué su distribución aproxima la distribución de muestreo del estimador en esta red recuperada. No se ha establecido un diseño probabilístico de selección de los registros que haga esa equivalencia automática.

Cuando se duplican internamente todas las respuestas de un investigador, la parte Bernoulli se duplica, pero la contribución de φσ sigue correspondiendo a un solo efecto aleatorio. A b y σ fijos, la información condicional de las respuestas se duplica; la precisión de la distribución normal, 1/σ², permanece igual. Si las multiplicidades son desiguales, cambia además la composición relativa de primeras/no primeras firmas y sus covariables dentro de cada historial.

En cambio, duplicar externamente un investigador completo conserva el balance de respuestas y densidad normal en cada copia independiente. Las dos operaciones coinciden en el límite sin heterogeneidad, σ→0, pero en general no con σ>0. El desplazamiento de σ de la auditoría anterior es coherente con este cambio; **por sí solo no demuestra la cobertura ni el sesgo de cada coeficiente fijo**.

## 4. Casos controlados pequeños

Se utilizaron dos investigadores con cuatro respuestas y dos columnas sintéticas de diseño, sin intervenir sobre CO2. A θ fijo, se compararon las funciones objetivo ponderadas con datos clonados explícitamente. También se verificó la suma de scores individuales frente al gradiente total y frente a diferencias finitas.

| Comprobación | Resultado |
| --- | --- |
| Pesos externos vs copias con nuevos IDs de investigador | Error absoluto 0.00e+00 |
| Pesos internos vs respuestas duplicadas con el mismo efecto aleatorio | Error absoluto 0.00e+00 |
| Pesos cruzados vs clonación literal de ambas dimensiones | Error absoluto 0.00e+00 |
| Duplicar todo externamente: −log L | 7.943093022 |
| Duplicar todo internamente: −log L | 7.775700941 |
| Diferencia interna−externa con σ=1,2 | -0.167392081 |
| Diferencia en el límite σ≈0 | 1.84e-12 |
| Suma de scores por investigador vs gradiente total | Error máximo 0.00e+00 |
| Gradiente analítico vs diferencias finitas | Error máximo 2.52e-11 |

En el ejemplo de σ=1,2, la precisión normal es 0,694444. La información condicional de las dos respuestas del primer investigador, evaluada en b=0, es 0,469229; duplicarlas internamente la lleva a 0,938459, mientras la precisión normal sigue siendo 0,694444. No es una estimación de información poblacional: es una comprobación local del balance de la función objetivo.

## 5. Alternativa elegida y fundamento

Se eligió la covarianza de scores por bloques porque evita intervenir sobre los productos Bernoulli o las distribuciones de efectos aleatorios y mantiene exactamente el estimador original. Para un bloque de dependencia k que contiene investigadores completos:

\[
S_k(\hat\theta)=\sum_{i\in k}\frac{\partial\log L_i(\hat\theta)}{\partial\theta},\qquad
H=-\frac{\partial^2\ell(\hat\theta)}{\partial\theta\partial\theta^\top}.
\]

Con K bloques, la implementación evaluada utiliza

\[
\widehat V=H^{-1}\left[
\frac{K}{K-1}\sum_k(S_k-\bar S)(S_k-\bar S)^\top
\right]H^{-1}.
\]

La Hessiana incluye el nuisance log σ; no se finge que σ sea conocido. Los intervalos para una pendiente se construyen con \(t_{K-1}\), una convención finita evaluada en las simulaciones, no una distribución exacta garantizada. No se propone un intervalo validado para σ.

El fundamento es la inferencia por ecuaciones de estimación con bloques independientes y un número suficiente de bloques que no dominen la suma de scores (Hansen & Lee, 2019; MacKinnon et al., 2023). La independencia debe justificarse; no se obtiene de contar componentes del grafo. Una covarianza robusta tampoco corrige una función media mal especificada ni convierte un OR de trabajo en un efecto causal.

## 6. Evaluación anterior a cualquier aplicación a CO2

Se simularon **500 conjuntos por escenario**, 1.500 en total. El protocolo, semillas y criterios se fijaron antes de los cálculos. Cada conjunto utiliza intercepto y una covariable sintética; no se agregan predictores al análisis CO2.

- **A — Logístico-normal equilibrado:** 40 bloques independientes, cuatro investigadores por bloque y seis observaciones por investigador. β=(−0,4; 0,6). El efecto aleatorio es suma de un componente de bloque con desviación 0,6 y uno individual con desviación 0,8; por ello el σ marginal verdadero por investigador es 1. Se conoce tanto la pendiente 0,6 como σ=1.
- **B — Firma única equilibrada:** 40 bloques de cuatro investigadores, seis publicaciones por equipo y una única primera firma por publicación, generada categóricamente a partir de habilidades latentes. La covariable no interviene en la asignación y es independiente de las habilidades: la pendiente nula objetivo es 0. El σ del GLMM de trabajo no se equipara a la desviación de las habilidades de este mecanismo.
- **C — Firma única con bloque dominante:** como B, pero un bloque incluye 80 investigadores en 20 equipos, frente a cuatro investigadores en cada uno de los otros 39 bloques. El primero aporta 33,9% de las observaciones y comparte un shock entre sus equipos. Se conoce la pendiente nula 0. Es una prueba de concentración, no una réplica exacta de CO2.

A diferencia del control paramétrico de la auditoría v0.1, B y C **sí respetan una única primera firma por artículo**. Su alcance es la calibración de la pendiente nula; no valida asociaciones no nulas de H1/H2 ni la interpretación de σ bajo ese mecanismo.

| Escenario | Utilizables | Cobertura nominal 95% | IC Wilson de cobertura | Error MC | Sesgo medio pendiente | SD empírica / SE estimado medio | Criterio previo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0: logístico-normal, bloques equilibrados | 500/500 | 94.4% | 92.03–96.10% | 1.03 pp | -0.0023 | 0.0875 / 0.0830 | Superado |
| 1: primera firma única, bloques equilibrados | 500/500 | 97.2% | 95.36–98.32% | 0.74 pp | -0.0069 | 0.0850 / 0.0894 | No superado |
| 2: primera firma única, bloque dominante | 500/500 | 93.6% | 91.10–95.43% | 1.09 pp | -0.0028 | 0.0729 / 0.0697 | Superado |

En A, la mediana estimada de σ fue 0,965 frente al valor generador conocido de 1; esto es una comprobación del parámetro de heterogeneidad, no una validación de intervalos para σ.

Las barras Wilson describen incertidumbre de Monte Carlo sobre la proporción de cobertura; **no son intervalos para un parámetro CO2**. Las réplicas no utilizables se habrían contado como no cobertura; no se sustituyeron según resultados favorables. En esta ejecución todas las 1.500 fueron utilizables. El código conserva los diagnósticos de optimización, integración, Hessiana y suma de scores.

![Calibración del candidato](figures/calibracion_candidato.png)

El criterio previo exigía al menos 98% de conjuntos utilizables en cada escenario, cobertura entre 92,5% y 97,5% y un intervalo Wilson que incluyera 95% en **todos** los escenarios. B presenta sobrecobertura y su intervalo Wilson no incluye 95%; por ello el candidato no supera el criterio completo. La sobrecobertura es compatible con intervalos conservadores y no equivale a infracobertura. Este resultado no habilita una afirmación de calibración nominal conforme al criterio elegido; tampoco es una prueba de invalidez universal. El criterio es conservador y hay error de Monte Carlo y multiplicidad entre escenarios; no se reajustó después de observar resultados.

**Decisión:** no aplicar el candidato a CO2 ni generar nuevos intervalos para H1/H2 con él. Incluso superar estas pruebas habría sido solo una condición necesaria: no habría demostrado independencia entre los componentes reales ni calibración de todos los contrastes y probabilidades.

## 7. Qué puede reportarse

| Resultado | Recomendación |
| --- | --- |
| Tamaños de muestra, frecuencias y marcas de calidad | Reportar con versión, denominadores y alcance documental. |
| β, OR y probabilidades de los ajustes originales | Reportar como resúmenes exploratorios del modelo de trabajo; conservar controles y antecedentes mixtos, sin afirmaciones causales, exclusivamente intraindividuales o de liderazgo demostrado. |
| σ original | Puede documentarse como parámetro nuisance/heterogeneidad latente del modelo de trabajo, con su escala y supuestos; no como desviación observada o estimación poblacional validada. |
| Intervalos Hessianos originales | Solo si se etiquetan explícitamente como dependientes de los supuestos no verificados de la verosimilitud de trabajo; no presentarlos como corrección por publicaciones compartidas ni como base para validar H1/H2. |
| Percentiles cruzados anteriores de β, probabilidades y σ | Mantener exclusivamente diagnósticos; no denominarlos incertidumbre robusta validada. |
| Distribuciones de remuestreo solo por investigador, componentes o paramétricas de v0.1 | Mantener diagnósticas; proximidad de la mediana de σ al original no acredita cobertura de β. |
| Coberturas, errores MC y resultados de casos pequeños de esta revisión | Reportar como evidencia metodológica con su DGP y alcance; no extrapolar su incertidumbre a CO2. |
| Sandwich candidato aplicado a CO2 | No aplicado. No se crean intervalos, p-valores ni decisiones nuevas de H1/H2. |

No es correcto concluir que H1 queda respaldada porque sus dos estimaciones puntuales tienen las direcciones previstas, ni que H2 queda refutada porque el coeficiente de constraint sea positivo. La recomendación sobre la evidencia inferencial disponible sigue siendo conservar ambos patrones como exploratorios.

## 8. Aclaración respecto de la auditoría anterior

Se precisa la expresión «anomalía de ponderación interna»: describe un comportamiento del esquema de remuestreo y de su objetivo integrado, **no un fallo demostrado de implementación del esquema cruzado previsto**. Las identidades de clonación descartan esa interpretación. La auditoría original queda conservada; esta revisión complementa su diagnóstico con pruebas de igualdad de funciones objetivo y una evaluación de cobertura con parámetros conocidos.

No se ha demostrado que cualquier remuestreo cruzado sea inválido ni que baste elevar también φσ a una potencia, normalizar los pesos dentro de cada investigador o cambiar identificadores de forma arbitraria. Cada modificación requiere especificar qué experimento de muestreo o superpoblación representa y validar su distribución para el estimando de interés.

## Reproducción y fuentes

El paquete contiene el protocolo previo, casos controlados, 1.500 resultados individuales, resumen de cobertura con incertidumbre Monte Carlo, decisión registrada, figura, código y requisitos. No requiere nuevas fuentes documentales ni acceso a los datos CO2 para reproducir las simulaciones. Se verificó por hashes que los ajustes originales y la auditoría permanecen intactos.

Hansen, B. E., & Lee, S. (2019). Asymptotic theory for clustered samples. *Journal of Econometrics, 210*(2), 268–290. https://doi.org/10.1016/j.jeconom.2019.02.001

MacKinnon, J. G., Nielsen, M. Ø., & Webb, M. D. (2023). Cluster-robust inference: A guide to empirical practice. *Journal of Econometrics, 232*(2), 272–299. https://doi.org/10.1016/j.jeconom.2022.04.001
