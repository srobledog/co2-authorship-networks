# Diccionario y claves de la muestra analítica v0.1

Los campos heredados mantienen las definiciones del diccionario v0.2.2 incluido. No se recodifica desconocido como no. La tabla de observaciones conserva todas las columnas de autoría previas y todas las columnas no redundantes del contexto.

| Campo o archivo | Definición |
|---|---|
| context_id | Clave estable investigador–año; única en contextos. |
| node_id | Identidad del investigador según la base corregida, sin nuevas fusiones. |
| work_id | Documento deduplicado; node_id+work_id es la clave de observaciones. |
| outcome_year, window_start, window_end | Año bibliográfico aplicado y límites t−3 y t−1. |
| sample_version | analytical_v0.1_base_v0.2.2; capa derivada, no corrección de v0.2.2. |
| n_sample_contexts_researcher | Contextos del investigador dentro de esta rama, no en toda su historia. |
| has_repeated_sample_contexts | Verdadero si tiene al menos dos contextos en la rama. |
| quality_partial_ego_document | ego_n_documents_partial>0; soporte de vínculos focal–alter o alter–alter. |
| quality_provisional_alter | n_alters_provisional>0; NAME o NAMEEMAIL entre colaboradores. |
| quality_joint_exclusion | Unión lógica de las dos marcas anteriores. |
| quality_overlap | neither / partial_only / provisional_only / both. |
| signing_role | Firma actual first/nonfirst en coautoría, utilizable según elegibilidad heredada. |
| prior_signing_group | exclusively_first_observed / exclusively_nonfirst_observed / mixed; solo firmas previas utilizables. |
| current_signature_category | first_only / nonfirst_only / both entre resultados elegibles del contexto. |
| n_outcome_observations, n_first, n_nonfirst | Observaciones actuales y desglose por firma en el contexto. |
| signature_category_varies_temporally | Al menos dos contextos con categorías actuales diferentes. |
| both_roles_observed_in_different_years | Existe firma primera en un año y no primera en otro, sin secuencia intranual. |
| has_first_only_and_nonfirst_only_years | Existe un año exclusivamente primero y otro exclusivamente no primero. |
| signature_variation_status | insufficient_years / varies / constant para categoría anual. |
| within_range | Máximo menos mínimo del indicador en contextos definidos de la persona; NA con menos de dos. |
| within_sd | Desviación estándar muestral entre contextos definidos; NA con menos de dos. |
| variation_status | insufficient_defined_contexts / varies (rango>1e−10) / constant. |
| n_defined, researchers_comparable | Valores por persona e investigadores con al menos dos valores definidos, respectivamente. |
| branch | principal / sin_parciales_ni_alters_provisionales. |
| subset | all / one_context / repeated_contexts, calculado dentro de rama. |
| membership | thematic / reference / both. both se cuenta una vez y pertenece al corpus temático. |
| position_independently_checked | Contraste independiente heredado de esta autoría; no se extiende a otras autorías. |
| ego_n_documents_* | Marcas heredadas sobre soporte de vínculos del ego. |
| normalization_n_documents_* | Marcas sobre soporte ampliado de denominadores de constraint/tamaño efectivo. |
| correlaciones_descriptivas.csv | Pearson y Spearman por pares de contextos completos, sin p-valores. |

Los indicadores se miden una vez por contexto, antes del resultado. Las firmas, títulos y procedencias corresponden a la publicación actual. Conteos de investigadores o documentos por categorías pueden solaparse. La sensibilidad conserva las otras marcas, no garantiza validación completa.
