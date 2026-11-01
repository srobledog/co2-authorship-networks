# CO2 — Dictamen sobre los bloques de dependencia
**Revisión documental v0.1 · 31 de octubre de 2026**

**Dictamen: TODAVÍA INCIERTO.** La independencia aproximada entre los 141 bloques no está acreditada por su construcción. Los registros muestran conexiones excluidas de esa regla, pero compartir documentos, autores o predictores no demuestra por sí mismo dependencia residual. No corresponde declarar independencia confirmada, ni fusionar todos los bloques automáticamente.

Se mantiene la orientación marginal por observación elegible y el GLMM como referencia exploratoria. No se ejecutaron modelos, diagnósticos de residuos ni simulaciones; no se modificaron datos, indicadores, hipótesis, manuscrito, pertenencia a bloques o criterios de evaluación.

## Cómo se construyeron

La auditoría v0.1 partió de las **1.079 observaciones principales hasta 2025**, correspondientes a 292 investigadores, 717 contextos y 765 publicaciones. Creó una conexión entre dos investigadores solo cuando ambos tenían una observación resultado elegible para el mismo work_id. La clausura transitiva de esas conexiones produjo 141 componentes. Todas las observaciones y años de un investigador quedaron en el mismo bloque; cada publicación resultado compartida por elegibles quedó dentro de un único bloque.

Así se incorporan la repetición del focal y la primera firma única de un artículo cuando hay varios focales elegibles. La regla no incorporó toda la red previa, todos los autores recuperados de los resultados ni los terceros usados en la normalización. Son componentes del grafo de observaciones elegibles, no los componentes de la red ampliada completa.

Se conservaron los bloques originales: 101 contienen un solo investigador; el mayor reúne 53 investigadores y 339 observaciones (31,4%), y los dos mayores, 43,5% de las filas. La concentración es una limitación adicional para inferencia, distinta de demostrar dependencia entre bloques.

## Qué conexiones quedaron fuera

Se filtraron los soportes existentes a los 717 contextos de la muestra principal. La tabla cuenta objetos distintos usados por dos o más bloques; las categorías se solapan y no deben sumarse.

| Objeto compartido | Cualquier año observado | Al menos un mismo año resultado t |
| --- | --- | --- |
| Publicación previa compartida por los focales | 76 | 45 |
| Colaborador previo común fuera de los 292 focales | 141 | 74 |
| Coautor común de publicaciones resultado, fuera de los 292 focales | 31 | 6 |
| Documento compartido de soporte de indicadores, cualquier función | 356 | 267 |
| Vínculo compartido utilizado en pesos/normalización de constraint | 1162 | 898 |
| Vínculo alter–tercero compartido fuera del ego inducido | 370 | 267 |

“Mismo año” alinea las ventanas [t−3,t−1] de los contextos comparados; no supone secuencia dentro del año ni cuenta cada objeto nuevamente por cada año. “Fuera de los 292 focales” significa no incluido como focal en la muestra principal; no significa que esa persona carezca de historia recuperada en toda la base.

Además, **92 personas que sí son focales en otros contextos** aparecen como autores recuperados sin fila elegible en **106 publicaciones resultado de otro bloque**. Esa coincidencia toca 84 pares de bloques. El artículo no conecta esos focales en la regla original porque uno de ellos carece de fila elegible para esa publicación. En cuatro de esas publicaciones, tres de estas identidades tienen resultados elegibles en otro bloque en el mismo año. Los demás cruces requieren considerar persistencia temporal; no se supone un shock contemporáneo por el solo enlace entre años.

También hay **245 publicaciones** que son resultado elegible de un bloque y soporte documental estrictamente previo de indicadores en otro. No significa que se copie su valor binario de primera firma al predictor: puede intervenir solo su coautoría o su peso de red. De esas publicaciones, 64 aparecen como colaboración previa del focal en algún contexto del otro bloque.

## Qué significan y qué no significan esas conexiones

| Conexión | Compartir información | Posible mecanismo residual, no demostrado |
| --- | --- | --- |
| Publicación previa común | Un mismo equipo/documento contribuye a varios antecedentes y redes previas. | Relaciones persistentes, recursos o shocks no recogidos por los controles pueden influir en resultados posteriores de ambos bloques. |
| Coautor común no elegible en los resultados | Un mismo participante está en distintos equipos, aunque no aporte filas analíticas propias. | Su participación o decisiones pueden afectar varias firmas posteriores. La falta de historia utilizable no elimina ese posible factor compartido. |
| Alter–alter o alter–tercero usado en indicadores | Densidad, pesos o fuerza total del alter comparten entradas observadas; la normalización de constraint alcanza fuera del ego inducido. | Errores de identidad/fecha compartidos o factores comunes persistentes pueden generar incertidumbre conjunta; un denominador compartido y correctamente observado no basta para afirmar correlación residual. |
| Resultado anterior de otro bloque usado como soporte | Hay enlace temporal entre el material que sustenta un resultado y un predictor posterior. | Se necesita un tratamiento coherente de historias predeterminadas; el enlace documental por sí solo no demuestra transmisión de errores. |

El grafo de solapamientos documenta procedencia y posibles mecanismos. No es una estimación de correlación, una prueba de independencia o una propuesta automática de nuevas unidades de jackknife. En particular, compartir un predictor o un dato fijo no exige agrupar las observaciones si la dependencia restante de las respuestas está adecuadamente condicionada. Tampoco tratar todos los predictores como fijos hace desaparecer factores comunes omitidos o errores compartidos de medición.

## Qué independencia necesita el procedimiento

Para el jackknife por bloques propuesto se necesita una justificación de independencia —o una aproximación suficientemente buena— entre las contribuciones de estimación de los bloques. En el modelo marginal esas contribuciones son S_g(β)=Σ_(r∈g) x_r[y_r−μ_r(β)]. La construcción actual asegura que ciertos eventos y personas queden juntos; no asegura que las contribuciones S_g y S_h de bloques distintos sean independientes.

Una condición suficiente sería que, bajo un tratamiento válido de las covariables e historias observadas, no quedaran perturbaciones relevantes compartidas de los resultados entre bloques. Una media residual cero por separado no garantiza esa condición: la varianza conjunta puede contener covarianzas cruzadas omitidas. Si se pretende una justificación asintótica más débil, debe establecerla el especialista; no se deduce de este inventario (Hansen & Lee, 2019).

Sería razonable defender una aproximación si conjuntamente se sostuviera que:

1. El soporte previo compartido se trata como información conocida/predeterminada bajo un esquema temporal coherente, con una media marginal adecuada para el estimando aceptado.
2. Las influencias persistentes de colaboradores comunes y los shocks compartidos no dejan dependencia residual material entre bloques después del condicionamiento defendido. No se presupone que nuestros controles ya consigan esto.
3. La incertidumbre común en las entradas de red es despreciable para esa inferencia condicionada, o se reconoce expresamente que queda fuera de su alcance.
4. No hay puentes adicionales relevantes ocultos por equipos incompletos, identidades inciertas o recuperación parcial. La aproximación tolerada y la influencia de los bloques grandes deben revisarse por separado.

Los registros no permiten verificar conjuntamente esas condiciones. Acreditan solapamientos, no su efecto residual. Por eso el supuesto queda **todavía incierto**, y no se habilita automáticamente la ejecución del jackknife o del generador.

## Decisión para la revisión metodológica conjunta

Mantener los 141 bloques como **definición observada de partida**, conservando el inventario de conexiones como evidencia. Clasificar con el especialista qué enlaces representan solo información condicionada y cuáles corresponden a un mecanismo de dependencia que el modelo no cubre. Solo después de esa discusión podría fijarse una definición distinta; esta etapa no la adopta.

Si se acepta independencia aproximada, debe quedar escrito qué mecanismos se están suponiendo despreciables y qué incertidumbre se condiciona. Si no puede justificarse, las conexiones no se “resuelven” suponiendo independencia ni agrupando toda la red sin criterio; corresponde revisar conjuntamente bloques, jackknife y generador antes de cualquier ejecución.

**Los criterios permanecen congelados:** 1.000 réplicas por escenario y máximo 3.000; utilizabilidad mínima 99%; tolerancia de sesgo estandarizado 0,2; cobertura mínima tolerable 92,5% para intervalos nominales del 95%, considerando incertidumbre Monte Carlo simultánea de los nueve resultados escenario–contraste; sobrecobertura no rechazada automáticamente; anchura y significación no seleccionan el método. Se conserva una copia exacta y su hash de la nota de estrategia existente. Aquí no se cambian esos criterios ni se ejecutan.

## Trazabilidad y límites

- Construcción original: `inference_audit_v01/code/audit.py`, función `structure`; pertenencia guardada en `row_component_membership.csv`.
- Soporte previo: tablas existentes `soporte_documental_y_calidad.csv` y `soporte_pesos_y_normalizacion.csv`, filtradas a los 717 contextos principales.
- Coautores recuperados y eventos: base corregida v0.2.2; no se recuperan autores nuevos ni se infieren historiales ausentes.
- Normalización: se rastrearon vínculos incidentes a alters, distinguiendo focal–alter, alter–alter y alter–tercero. La suma del peso documental rastreado coincide con las fuerzas previamente almacenadas en las 4.421 filas alter–contexto examinadas; no se recalcularon indicadores.
- Cobertura: de los 141 colaboradores previos compartidos fuera de los focales, cuatro tienen claves NAME/NAMEEMAIL provisionales. La ausencia de esa marca en otros IDs no prueba validación completa. Fechas, equipos e identidades conservan sus incertidumbres heredadas; los conteos son sobre la base recuperada, no tasas reales de conexiones faltantes.
- El paquete incluye inventarios por objeto y pares de bloques, traza de aristas, código descriptivo, hashes de entrada y criterios preservados. Los pares de bloques son tablas de exposición documental, no instrucciones de fusión.

## Referencias

Hansen, B. E., & Lee, S. (2019). Asymptotic theory for clustered samples. *Journal of Econometrics, 210*(2), 268–290. https://doi.org/10.1016/j.jeconom.2019.02.001

MacKinnon, J. G., Nielsen, M. Ø., & Webb, M. D. (2025). Cluster-robust jackknife and bootstrap inference for logistic regression models. *Econometric Reviews*. https://doi.org/10.1080/07474938.2025.2515161
