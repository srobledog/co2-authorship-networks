# Diccionario de la capa egocéntrica v0.2.2

Ventana de todas las medidas previas: t−3 a t−1. Los metadatos actuales están explícitamente separados. NA significa indefinido o no calculable según reglas, no cero.

| Archivo | Campo | Definición |
|---|---|---|
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| F6_at_least_two_collaborators_correlation_pairwise_n.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| F6_at_least_two_collaborators_correlation_pearson.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| F6_at_least_two_collaborators_correlation_pearson.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| F6_at_least_two_collaborators_correlation_pearson.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| F6_at_least_two_collaborators_correlation_pearson.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| F6_at_least_two_collaborators_correlation_pearson.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| F6_at_least_two_collaborators_correlation_pearson.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| F6_at_least_two_collaborators_correlation_pearson.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| F6_at_least_two_collaborators_correlation_pearson.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| F6_at_least_two_collaborators_correlation_pearson.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| F6_at_least_two_collaborators_correlation_pearson.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| F6_at_least_two_collaborators_correlation_pearson.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| F6_at_least_two_collaborators_correlation_pearson.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| F6_at_least_two_collaborators_correlation_pearson.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| F6_at_least_two_collaborators_correlation_pearson.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| F6_at_least_two_collaborators_correlation_pearson.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| F6_at_least_two_collaborators_correlation_spearman.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| F6_at_least_two_collaborators_correlation_spearman.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| F6_at_least_two_collaborators_correlation_spearman.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| F6_at_least_two_collaborators_correlation_spearman.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| F6_at_least_two_collaborators_correlation_spearman.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| F6_at_least_two_collaborators_correlation_spearman.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| F6_at_least_two_collaborators_correlation_spearman.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| F6_at_least_two_collaborators_correlation_spearman.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| F6_at_least_two_collaborators_correlation_spearman.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| F6_at_least_two_collaborators_correlation_spearman.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| F6_at_least_two_collaborators_correlation_spearman.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| F6_at_least_two_collaborators_correlation_spearman.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| F6_at_least_two_collaborators_correlation_spearman.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| F6_at_least_two_collaborators_correlation_spearman.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| F6_at_least_two_collaborators_correlation_spearman.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| F6_contexts_correlation_pairwise_n.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| F6_contexts_correlation_pairwise_n.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| F6_contexts_correlation_pairwise_n.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| F6_contexts_correlation_pairwise_n.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| F6_contexts_correlation_pairwise_n.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| F6_contexts_correlation_pairwise_n.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| F6_contexts_correlation_pairwise_n.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| F6_contexts_correlation_pairwise_n.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| F6_contexts_correlation_pairwise_n.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| F6_contexts_correlation_pairwise_n.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| F6_contexts_correlation_pairwise_n.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| F6_contexts_correlation_pairwise_n.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| F6_contexts_correlation_pairwise_n.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| F6_contexts_correlation_pairwise_n.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| F6_contexts_correlation_pairwise_n.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| F6_contexts_correlation_pearson.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| F6_contexts_correlation_pearson.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| F6_contexts_correlation_pearson.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| F6_contexts_correlation_pearson.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| F6_contexts_correlation_pearson.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| F6_contexts_correlation_pearson.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| F6_contexts_correlation_pearson.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| F6_contexts_correlation_pearson.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| F6_contexts_correlation_pearson.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| F6_contexts_correlation_pearson.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| F6_contexts_correlation_pearson.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| F6_contexts_correlation_pearson.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| F6_contexts_correlation_pearson.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| F6_contexts_correlation_pearson.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| F6_contexts_correlation_pearson.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| F6_contexts_correlation_spearman.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| F6_contexts_correlation_spearman.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| F6_contexts_correlation_spearman.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| F6_contexts_correlation_spearman.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| F6_contexts_correlation_spearman.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| F6_contexts_correlation_spearman.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| F6_contexts_correlation_spearman.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| F6_contexts_correlation_spearman.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| F6_contexts_correlation_spearman.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| F6_contexts_correlation_spearman.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| F6_contexts_correlation_spearman.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| F6_contexts_correlation_spearman.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| F6_contexts_correlation_spearman.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| F6_contexts_correlation_spearman.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| F6_contexts_correlation_spearman.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| all_current_position_coverage.csv | eligible_provisional | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| all_current_position_coverage.csv | signing_role | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| all_current_position_coverage.csv | observations | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| all_current_position_coverage.csv | researchers | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| all_observed_contexts_correlation_pairwise_n.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| all_observed_contexts_correlation_pairwise_n.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| all_observed_contexts_correlation_pairwise_n.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| all_observed_contexts_correlation_pairwise_n.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| all_observed_contexts_correlation_pairwise_n.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| all_observed_contexts_correlation_pairwise_n.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| all_observed_contexts_correlation_pairwise_n.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| all_observed_contexts_correlation_pairwise_n.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| all_observed_contexts_correlation_pairwise_n.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| all_observed_contexts_correlation_pairwise_n.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| all_observed_contexts_correlation_pairwise_n.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| all_observed_contexts_correlation_pairwise_n.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| all_observed_contexts_correlation_pairwise_n.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| all_observed_contexts_correlation_pairwise_n.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| all_observed_contexts_correlation_pairwise_n.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| all_observed_contexts_correlation_pearson.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| all_observed_contexts_correlation_pearson.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| all_observed_contexts_correlation_pearson.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| all_observed_contexts_correlation_pearson.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| all_observed_contexts_correlation_pearson.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| all_observed_contexts_correlation_pearson.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| all_observed_contexts_correlation_pearson.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| all_observed_contexts_correlation_pearson.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| all_observed_contexts_correlation_pearson.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| all_observed_contexts_correlation_pearson.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| all_observed_contexts_correlation_pearson.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| all_observed_contexts_correlation_pearson.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| all_observed_contexts_correlation_pearson.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| all_observed_contexts_correlation_pearson.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| all_observed_contexts_correlation_pearson.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| all_observed_contexts_correlation_spearman.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| all_observed_contexts_correlation_spearman.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| all_observed_contexts_correlation_spearman.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| all_observed_contexts_correlation_spearman.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| all_observed_contexts_correlation_spearman.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| all_observed_contexts_correlation_spearman.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| all_observed_contexts_correlation_spearman.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| all_observed_contexts_correlation_spearman.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| all_observed_contexts_correlation_spearman.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| all_observed_contexts_correlation_spearman.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| all_observed_contexts_correlation_spearman.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| all_observed_contexts_correlation_spearman.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| all_observed_contexts_correlation_spearman.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| all_observed_contexts_correlation_spearman.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| all_observed_contexts_correlation_spearman.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| alter_edge_document_provenance.csv | context_id | Clave única node_id + año t del resultado; unidad de cálculo. |
| alter_edge_document_provenance.csv | node_id | Identidad estable heredada de v0.2.2; no se unen personas. |
| alter_edge_document_provenance.csv | outcome_year | Año t del resultado; no pertenece a la ventana previa. |
| alter_edge_document_provenance.csv | Source | Identidad estable del extremo del vínculo o alter; nombres no se usan como claves. |
| alter_edge_document_provenance.csv | Target | Identidad estable del extremo del vínculo o alter; nombres no se usan como claves. |
| alter_edge_document_provenance.csv | weight | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_edge_document_provenance.csv | n_documents_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_edge_document_provenance.csv | n_documents_without_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_edge_document_provenance.csv | source_category | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_edge_document_provenance.csv | work_ids_with_focal | Identificador(es) de documento deduplicado v0.2.2 que permiten comprobar la medida. |
| alter_edge_document_provenance.csv | work_ids_without_focal | Identificador(es) de documento deduplicado v0.2.2 que permiten comprobar la medida. |
| alter_weights_and_normalization.csv | context_id | Clave única node_id + año t del resultado; unidad de cálculo. |
| alter_weights_and_normalization.csv | node_id | Identidad estable heredada de v0.2.2; no se unen personas. |
| alter_weights_and_normalization.csv | outcome_year | Año t del resultado; no pertenece a la ventana previa. |
| alter_weights_and_normalization.csv | alter_id | Identidad estable del extremo del vínculo o alter; nombres no se usan como claves. |
| alter_weights_and_normalization.csv | weight | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_weights_and_normalization.csv | n_distinct_years | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_weights_and_normalization.csv | repeated_publications | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_weights_and_normalization.csv | repeated_distinct_years | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_weights_and_normalization.csv | alter_strength_full_prior_graph | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_weights_and_normalization.csv | alter_max_weight_full_prior_graph | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| alter_weights_and_normalization.csv | work_ids | Identificador(es) de documento deduplicado v0.2.2 que permiten comprobar la medida. |
| closure_publication_provenance_summary.csv | scope | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| closure_publication_provenance_summary.csv | contexts | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| closure_publication_provenance_summary.csv | contexts_two_or_more | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | contexts_with_alter_edges | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | contexts_density_one | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | contexts_all_closure_edges_only_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | contexts_any_without_focal_support | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | contexts_one_prior_coauthor_doc_two_or_more | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | one_doc_contexts_density_one | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | sum_context_alter_edges | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | sum_context_edges_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | sum_context_edges_only_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | sum_context_edges_only_without_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | sum_context_edges_both | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | share_context_edges_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | share_context_edges_only_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | alter_pair_publication_events_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | alter_pair_publication_events_without_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| closure_publication_provenance_summary.csv | median_context_edge_share_supported_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | context_id | Clave única node_id + año t del resultado; unidad de cálculo. |
| context_document_support_and_quality.csv | node_id | Identidad estable heredada de v0.2.2; no se unen personas. |
| context_document_support_and_quality.csv | outcome_year | Año t del resultado; no pertenece a la ventana previa. |
| context_document_support_and_quality.csv | work_id | Identificador(es) de documento deduplicado v0.2.2 que permiten comprobar la medida. |
| context_document_support_and_quality.csv | document_year | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | focal_collaboration_document | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | alter_alter_document | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | normalization_only | Documento incidente a algún alter que no genera una arista del ego, pero interviene en la fuerza/máximo de normalización. |
| context_document_support_and_quality.csv | partial | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | size_conflict | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | uncertain_team | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | date_alert | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | date_unverified | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | endpoint_conflict | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | known_identity_unresolved | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | provisional | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | max_team | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | recovered_team | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| context_document_support_and_quality.csv | identity_not_documentary_checked | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| current_context_signature_categories.csv | context_id | Clave única node_id + año t del resultado; unidad de cálculo. |
| current_context_signature_categories.csv | node_id | Identidad estable heredada de v0.2.2; no se unen personas. |
| current_context_signature_categories.csv | prior_signing_group | Solo primeras previas observadas, solo no primeras o mixtas; solo firmas utilizables recuperadas. |
| current_context_signature_categories.csv | current_context_signature | Primera únicamente/no primera únicamente/ambas en los resultados elegibles de t; no ordena artículos. |
| current_context_signature_categories.csv | n_eligible_outcome_publications | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| current_signature_by_prior_group_contexts.csv | prior_signing_group | Solo primeras previas observadas, solo no primeras o mixtas; solo firmas utilizables recuperadas. |
| current_signature_by_prior_group_contexts.csv | current_context_signature | Primera únicamente/no primera únicamente/ambas en los resultados elegibles de t; no ordena artículos. |
| current_signature_by_prior_group_contexts.csv | contexts | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| current_signature_by_prior_group_contexts.csv | researchers | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| current_signature_by_prior_group_publications.csv | prior_signing_group | Solo primeras previas observadas, solo no primeras o mixtas; solo firmas utilizables recuperadas. |
| current_signature_by_prior_group_publications.csv | signing_role | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| current_signature_by_prior_group_publications.csv | outcome_publications | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| current_signature_by_prior_group_publications.csv | researchers | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| current_signature_by_prior_group_publications.csv | contexts | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| current_signature_by_prior_group_publications.csv | share_of_prior_group | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | context_id | Clave única node_id + año t del resultado; unidad de cálculo. |
| ego_context_indicators.csv | node_id | Identidad estable heredada de v0.2.2; no se unen personas. |
| ego_context_indicators.csv | label | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | outcome_year | Año t del resultado; no pertenece a la ventana previa. |
| ego_context_indicators.csv | window_start | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | window_end | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | context_eligible_F6 | Alguna publicación resultado del contexto cumple elegibilidad F6 de la base, sin cambiar criterios. |
| ego_context_indicators.csv | prior_signing_group | Solo primeras previas observadas, solo no primeras o mixtas; solo firmas utilizables recuperadas. |
| ego_context_indicators.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| ego_context_indicators.csv | collaborator_group | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| ego_context_indicators.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| ego_context_indicators.csv | n_prior_coauthor_publications_available_evidence | Documentos reconocibles como multiautor por evidencia disponible, aunque falten socios. |
| ego_context_indicators.csv | n_prior_coauthor_publications_no_recovered_partner | Diferencia entre documentos multiautor reconocibles y documentos con un vínculo recuperado. |
| ego_context_indicators.csv | n_focal_pair_document_events | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| ego_context_indicators.csv | n_possible_alter_edges | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| ego_context_indicators.csv | density_status | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| ego_context_indicators.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| ego_context_indicators.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| ego_context_indicators.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| ego_context_indicators.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| ego_context_indicators.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| ego_context_indicators.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| ego_context_indicators.csv | n_repeat_pair_events | Σ_j(w_ij−1)=eventos pareja–documento−colaboradores. |
| ego_context_indicators.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| ego_context_indicators.csv | mean_publications_per_alter | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | n_alters_repeated_distinct_years | Colaboradores que comparten documentos con focal en al menos dos años distintos de la ventana. |
| ego_context_indicators.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| ego_context_indicators.csv | n_alter_edges_with_focal_document | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | n_alter_edges_only_with_focal | Parejas alter–alter cuyos documentos de soporte de ventana incluyen siempre al focal. |
| ego_context_indicators.csv | n_alter_edges_only_without_focal | Parejas alter–alter sin documento compartido con focal en la ventana. |
| ego_context_indicators.csv | n_alter_edges_both_sources | Parejas con soporte tanto en documentos con focal como sin focal. |
| ego_context_indicators.csv | n_alter_pair_events_with_focal | Número de eventos alter–alter–documento de la ventana, según el documento contenga o no al focal. |
| ego_context_indicators.csv | n_alter_pair_events_without_focal | Número de eventos alter–alter–documento de la ventana, según el documento contenga o no al focal. |
| ego_context_indicators.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| ego_context_indicators.csv | share_alter_edges_exclusively_with_focal | Parejas solo con focal/M; NA cuando M=0. |
| ego_context_indicators.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| ego_context_indicators.csv | alter_density_exclusively_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | focal_identity_provisional | Marca de incertidumbre registrada en la base, no juicio de error ni completitud histórica. |
| ego_context_indicators.csv | n_alters_provisional | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | n_alters_with_label_variants | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | n_prior_coauthor_signatures_unknown | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | n_focal_documents_team_ge_10 | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | max_recovered_focal_team_size | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | n_current_publications | Metadato del resultado: publicaciones actuales del contexto. NO es predictor previo. |
| ego_context_indicators.csv | n_current_eligible_publications | Metadato del resultado: publicaciones actuales F6. NO es predictor previo. |
| ego_context_indicators.csv | ego_n_support_documents | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | ego_n_documents_partial | Número de documentos distintos del soporte del ego con la marca partial. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | ego_n_documents_size_conflict | Número de documentos distintos del soporte del ego con la marca size_conflict. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | ego_n_documents_uncertain_team | Número de documentos distintos del soporte del ego con la marca uncertain_team. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | ego_n_documents_date_alert | Número de documentos distintos del soporte del ego con la marca date_alert. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | ego_n_documents_date_unverified | Número de documentos distintos del soporte del ego con la marca date_unverified. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | ego_n_documents_endpoint_conflict | Número de documentos distintos del soporte del ego con la marca endpoint_conflict. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | ego_n_documents_known_identity_unresolved | Número de documentos distintos del soporte del ego con la marca known_identity_unresolved. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | ego_n_documents_provisional | Número de documentos distintos del soporte del ego con la marca provisional. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | ego_n_documents_identity_not_documentary_checked | Número de documentos distintos del soporte del ego con la marca identity_not_documentary_checked. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | ego_has_recorded_uncertainty | Marca de incertidumbre registrada en la base, no juicio de error ni completitud histórica. |
| ego_context_indicators.csv | normalization_n_support_documents | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| ego_context_indicators.csv | normalization_n_documents_partial | Número de documentos distintos del soporte de normalización completa con la marca partial. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | normalization_n_documents_size_conflict | Número de documentos distintos del soporte de normalización completa con la marca size_conflict. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | normalization_n_documents_uncertain_team | Número de documentos distintos del soporte de normalización completa con la marca uncertain_team. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | normalization_n_documents_date_alert | Número de documentos distintos del soporte de normalización completa con la marca date_alert. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | normalization_n_documents_date_unverified | Número de documentos distintos del soporte de normalización completa con la marca date_unverified. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | normalization_n_documents_endpoint_conflict | Número de documentos distintos del soporte de normalización completa con la marca endpoint_conflict. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | normalization_n_documents_known_identity_unresolved | Número de documentos distintos del soporte de normalización completa con la marca known_identity_unresolved. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | normalization_n_documents_provisional | Número de documentos distintos del soporte de normalización completa con la marca provisional. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | normalization_n_documents_identity_not_documentary_checked | Número de documentos distintos del soporte de normalización completa con la marca identity_not_documentary_checked. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| ego_context_indicators.csv | normalization_has_recorded_uncertainty | Marca de incertidumbre registrada en la base, no juicio de error ni completitud histórica. |
| ego_context_indicators.csv | n_prior_focal_partial_team_documents | Conteo de documentos previos del propio focal con la condición indicada; incluye cobertura sin socio recuperado. |
| ego_context_indicators.csv | n_prior_focal_date_alert_documents | Conteo de documentos previos del propio focal con la condición indicada; incluye cobertura sin socio recuperado. |
| ego_context_indicators.csv | n_prior_focal_uncertain_team_documents | Conteo de documentos previos del propio focal con la condición indicada; incluye cobertura sin socio recuperado. |
| ego_context_indicators.csv | prior_focal_coverage_uncertain | Hay antecedentes focales parciales, con fecha alertada, equipo incierto o sin socio recuperado; no implica error confirmado. |
| focal_coauthor_documents_without_recovered_partner.csv | context_id | Clave única node_id + año t del resultado; unidad de cálculo. |
| focal_coauthor_documents_without_recovered_partner.csv | node_id | Identidad estable heredada de v0.2.2; no se unen personas. |
| focal_coauthor_documents_without_recovered_partner.csv | outcome_year | Año t del resultado; no pertenece a la ventana previa. |
| focal_coauthor_documents_without_recovered_partner.csv | work_id | Identificador(es) de documento deduplicado v0.2.2 que permiten comprobar la medida. |
| focal_coauthor_documents_without_recovered_partner.csv | document_year | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| focal_coauthor_documents_without_recovered_partner.csv | n_authors_recovered | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| focal_coauthor_documents_without_recovered_partner.csv | n_authors_evidence_max | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| focal_coauthor_documents_without_recovered_partner.csv | team_partial | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| focal_coauthor_documents_without_recovered_partner.csv | date_uncertainty_flag | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| focal_coauthor_documents_without_recovered_partner.csv | position_usable | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| focal_coauthor_documents_without_recovered_partner.csv | reason | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| formula_matrix_checks.csv | context_id | Clave única node_id + año t del resultado; unidad de cálculo. |
| formula_matrix_checks.csv | constraint_matrix | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| formula_matrix_checks.csv | effective_matrix | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| indicator_correlations_pairwise.csv | scope | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| indicator_correlations_pairwise.csv | indicator_1 | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| indicator_correlations_pairwise.csv | indicator_2 | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| indicator_correlations_pairwise.csv | n_context_pairs | Número de contextos únicos que sustentan esa correlación. |
| indicator_correlations_pairwise.csv | n_researchers | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| indicator_correlations_pairwise.csv | pearson | Correlación descriptiva por pares completos de contextos; NA con n<3 o variable constante. |
| indicator_correlations_pairwise.csv | spearman | Pearson de rangos medios calculados dentro del mismo par completo; sin p-valores. |
| indicator_correlations_pairwise.csv | status | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| indicator_distributions.csv | scope | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| indicator_distributions.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| indicator_distributions.csv | contexts | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| indicator_distributions.csv | defined | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| indicator_distributions.csv | missing | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| indicator_distributions.csv | zero | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| indicator_distributions.csv | one | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| indicator_distributions.csv | min | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| indicator_distributions.csv | p05 | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| indicator_distributions.csv | q25 | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| indicator_distributions.csv | median | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| indicator_distributions.csv | q75 | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| indicator_distributions.csv | p95 | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| indicator_distributions.csv | max | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| indicator_distributions.csv | mean | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| indicator_distributions.csv | sd | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| indicator_distributions.csv | distinct_values | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| missingness_reasons.csv | scope | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| missingness_reasons.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| missingness_reasons.csv | reason | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| missingness_reasons.csv | missing | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| missingness_reasons.csv | reason_groups_overlap | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | node_id | Identidad estable heredada de v0.2.2; no se unen personas. |
| outcomes_linked_to_ego_context.csv | label | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | work_id | Identificador(es) de documento deduplicado v0.2.2 que permiten comprobar la medida. |
| outcomes_linked_to_ego_context.csv | title | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | doi | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | year | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | year_values | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | year_rule | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | document_sources | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | ordinal_source | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | original_export_years | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | original_export_year_variation | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | original_export_max_year_disagrees | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | date_conflict | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | external_print_year_disagreement | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | date_uncertainty_flag | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | cached_print_years | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | cached_online_years | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | date_validation_status | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | is_thematic | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | is_reference | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | membership | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | author_position | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | position_numeric_valid | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | position_status | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | position_usable | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | position_independently_checked | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | coauthor_publication | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | signing_role | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_authors_recovered | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_authors_evidence_max | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | single_author_status | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | team_partial | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | team_size_conflict | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | selected_team_has_prior_quarantined_conflicts | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | identity_provisional | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | identity_label_variants | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | name_or_order_conflict | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | source_authorship_row | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | input_article_rows | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | position_evidence | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | independent_position_candidates | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | year_is_2026 | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | year_before_v021 | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | documentary_scope_v022 | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | context_id | Clave única node_id + año t del resultado; unidad de cálculo. |
| outcomes_linked_to_ego_context.csv | outcome_year | Año t del resultado; no pertenece a la ventana previa. |
| outcomes_linked_to_ego_context.csv | window_start | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | window_end | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_publications_prior_window | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_coauthor_publications_prior_window | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_usable_coauthor_signatures_prior_window | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_independently_checked_signatures_prior_window | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_usable_individual_signatures_prior_window | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | prior_signing_group | Solo primeras previas observadas, solo no primeras o mixtas; solo firmas utilizables recuperadas. |
| outcomes_linked_to_ego_context.csv | n_unknown_coauthor_signatures_prior_window | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_uncertain_team_documents_prior_window | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | prior_roles_complete_among_recovered_coauthor_docs | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | prior_roles_and_team_types_resolved | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_collaborators | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | prior_collaborator_group | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_collaboration_events | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_collaborators_provisional | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_events_endpoint_name_conflict | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_partial_team_documents | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_date_conflict_documents | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_alter_alter_edges | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_alter_alter_events | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_name_or_order_conflict_documents | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | has_earlier_observed_year | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | has_later_observed_year | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | eligible_provisional | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | eligible_low_recorded_uncertainty | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | first_exclusion_or_eligibility | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | context_eligible_F6 | Alguna publicación resultado del contexto cumple elegibilidad F6 de la base, sin cambiar criterios. |
| outcomes_linked_to_ego_context.csv | n_collaborators | Número de vecinos distintos del focal con al menos una coautoría identificada en t−3 a t−1. |
| outcomes_linked_to_ego_context.csv | collaborator_group | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| outcomes_linked_to_ego_context.csv | n_prior_coauthor_publications_with_identified_partner | Documentos distintos del focal con al menos un socio recuperado en la ventana. |
| outcomes_linked_to_ego_context.csv | n_prior_coauthor_publications_available_evidence | Documentos reconocibles como multiautor por evidencia disponible, aunque falten socios. |
| outcomes_linked_to_ego_context.csv | n_prior_coauthor_publications_no_recovered_partner | Diferencia entre documentos multiautor reconocibles y documentos con un vínculo recuperado. |
| outcomes_linked_to_ego_context.csv | n_focal_pair_document_events | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_alter_edges | Parejas distintas entre los colaboradores del focal con alguna publicación previa compartida. |
| outcomes_linked_to_ego_context.csv | n_possible_alter_edges | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | alter_density | 2*n_alter_edges/[n_collaborators*(n_collaborators−1)]; NA para n<2. |
| outcomes_linked_to_ego_context.csv | density_status | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| outcomes_linked_to_ego_context.csv | burt_constraint_weighted | Σ_j[p_ij+Σ_q p_iq p_qj]^2; p normalizado por fuerza sobre red previa completa observada; NA aislados. |
| outcomes_linked_to_ego_context.csv | effective_size_weighted | Σ_j[1−Σ_q p_iq m_jq]; m normalizado por máximo peso del alter sobre toda la red previa observada. |
| outcomes_linked_to_ego_context.csv | effective_efficiency_weighted | Tamaño efectivo ponderado/n; NA con n=0. |
| outcomes_linked_to_ego_context.csv | effective_size_binary | n−2*M/n; control binario matemáticamente dependiente de n y densidad. |
| outcomes_linked_to_ego_context.csv | n_repeated_alters | Número de colaboradores con al menos dos documentos compartidos en la ventana. |
| outcomes_linked_to_ego_context.csv | share_repeated_alters | Colaboradores repetidos/n; NA con n=0. |
| outcomes_linked_to_ego_context.csv | n_repeat_pair_events | Σ_j(w_ij−1)=eventos pareja–documento−colaboradores. |
| outcomes_linked_to_ego_context.csv | share_repeat_pair_events | Exceso de eventos pareja–documento / total de eventos focal–alter; NA sin eventos. |
| outcomes_linked_to_ego_context.csv | mean_publications_per_alter | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_alters_repeated_distinct_years | Colaboradores que comparten documentos con focal en al menos dos años distintos de la ventana. |
| outcomes_linked_to_ego_context.csv | share_alters_repeated_distinct_years | Número anterior/n; no ordena artículos intranuales. |
| outcomes_linked_to_ego_context.csv | n_alter_edges_with_focal_document | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_alter_edges_only_with_focal | Parejas alter–alter cuyos documentos de soporte de ventana incluyen siempre al focal. |
| outcomes_linked_to_ego_context.csv | n_alter_edges_only_without_focal | Parejas alter–alter sin documento compartido con focal en la ventana. |
| outcomes_linked_to_ego_context.csv | n_alter_edges_both_sources | Parejas con soporte tanto en documentos con focal como sin focal. |
| outcomes_linked_to_ego_context.csv | n_alter_pair_events_with_focal | Número de eventos alter–alter–documento de la ventana, según el documento contenga o no al focal. |
| outcomes_linked_to_ego_context.csv | n_alter_pair_events_without_focal | Número de eventos alter–alter–documento de la ventana, según el documento contenga o no al focal. |
| outcomes_linked_to_ego_context.csv | share_alter_edges_supported_with_focal | Parejas con algún documento con focal/M; NA cuando M=0. |
| outcomes_linked_to_ego_context.csv | share_alter_edges_exclusively_with_focal | Parejas solo con focal/M; NA cuando M=0. |
| outcomes_linked_to_ego_context.csv | alter_density_supported_without_focal | (Parejas solo sin focal + ambas)/n(n−1)/2; NA n<2. |
| outcomes_linked_to_ego_context.csv | alter_density_exclusively_with_focal | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | focal_identity_provisional | Marca de incertidumbre registrada en la base, no juicio de error ni completitud histórica. |
| outcomes_linked_to_ego_context.csv | n_alters_provisional | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_alters_with_label_variants | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_prior_coauthor_signatures_unknown | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_focal_documents_team_ge_10 | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | max_recovered_focal_team_size | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | n_current_publications | Metadato del resultado: publicaciones actuales del contexto. NO es predictor previo. |
| outcomes_linked_to_ego_context.csv | n_current_eligible_publications | Metadato del resultado: publicaciones actuales F6. NO es predictor previo. |
| outcomes_linked_to_ego_context.csv | ego_n_support_documents | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | ego_n_documents_partial | Número de documentos distintos del soporte del ego con la marca partial. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | ego_n_documents_size_conflict | Número de documentos distintos del soporte del ego con la marca size_conflict. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | ego_n_documents_uncertain_team | Número de documentos distintos del soporte del ego con la marca uncertain_team. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | ego_n_documents_date_alert | Número de documentos distintos del soporte del ego con la marca date_alert. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | ego_n_documents_date_unverified | Número de documentos distintos del soporte del ego con la marca date_unverified. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | ego_n_documents_endpoint_conflict | Número de documentos distintos del soporte del ego con la marca endpoint_conflict. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | ego_n_documents_known_identity_unresolved | Número de documentos distintos del soporte del ego con la marca known_identity_unresolved. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | ego_n_documents_provisional | Número de documentos distintos del soporte del ego con la marca provisional. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | ego_n_documents_identity_not_documentary_checked | Número de documentos distintos del soporte del ego con la marca identity_not_documentary_checked. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | ego_has_recorded_uncertainty | Marca de incertidumbre registrada en la base, no juicio de error ni completitud histórica. |
| outcomes_linked_to_ego_context.csv | normalization_n_support_documents | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| outcomes_linked_to_ego_context.csv | normalization_n_documents_partial | Número de documentos distintos del soporte de normalización completa con la marca partial. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | normalization_n_documents_size_conflict | Número de documentos distintos del soporte de normalización completa con la marca size_conflict. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | normalization_n_documents_uncertain_team | Número de documentos distintos del soporte de normalización completa con la marca uncertain_team. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | normalization_n_documents_date_alert | Número de documentos distintos del soporte de normalización completa con la marca date_alert. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | normalization_n_documents_date_unverified | Número de documentos distintos del soporte de normalización completa con la marca date_unverified. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | normalization_n_documents_endpoint_conflict | Número de documentos distintos del soporte de normalización completa con la marca endpoint_conflict. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | normalization_n_documents_known_identity_unresolved | Número de documentos distintos del soporte de normalización completa con la marca known_identity_unresolved. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | normalization_n_documents_provisional | Número de documentos distintos del soporte de normalización completa con la marca provisional. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | normalization_n_documents_identity_not_documentary_checked | Número de documentos distintos del soporte de normalización completa con la marca identity_not_documentary_checked. Marcas de auditoría, no errores confirmados; categorías pueden solaparse. |
| outcomes_linked_to_ego_context.csv | normalization_has_recorded_uncertainty | Marca de incertidumbre registrada en la base, no juicio de error ni completitud histórica. |
| outcomes_linked_to_ego_context.csv | n_prior_focal_partial_team_documents | Conteo de documentos previos del propio focal con la condición indicada; incluye cobertura sin socio recuperado. |
| outcomes_linked_to_ego_context.csv | n_prior_focal_date_alert_documents | Conteo de documentos previos del propio focal con la condición indicada; incluye cobertura sin socio recuperado. |
| outcomes_linked_to_ego_context.csv | n_prior_focal_uncertain_team_documents | Conteo de documentos previos del propio focal con la condición indicada; incluye cobertura sin socio recuperado. |
| outcomes_linked_to_ego_context.csv | prior_focal_coverage_uncertain | Hay antecedentes focales parciales, con fecha alertada, equipo incierto o sin socio recuperado; no implica error confirmado. |
| researcher_context_counts.csv | scope | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| researcher_context_counts.csv | node_id | Identidad estable heredada de v0.2.2; no se unen personas. |
| researcher_context_counts.csv | label | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| researcher_context_counts.csv | n_eligible_contexts | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| researcher_context_counts.csv | context_count_category | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| researcher_context_counts.csv | outcome_years | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| uncertainty_context_summary.csv | scope | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| uncertainty_context_summary.csv | flag | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| uncertainty_context_summary.csv | contexts_affected | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| uncertainty_context_summary.csv | contexts | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| uncertainty_context_summary.csv | percent | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| uncertainty_context_summary.csv | sum_counts | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| within_researcher_variation.csv | scope | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| within_researcher_variation.csv | node_id | Identidad estable heredada de v0.2.2; no se unen personas. |
| within_researcher_variation.csv | label | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| within_researcher_variation.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| within_researcher_variation.csv | n_contexts | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| within_researcher_variation.csv | n_defined | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| within_researcher_variation.csv | n_distinct_values | Conteo explícito en la unidad y universo de esta tabla; faltantes no se convierten en cero. |
| within_researcher_variation.csv | min | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| within_researcher_variation.csv | max | Resumen descriptivo de valores definidos en el universo indicado; un contexto cuenta una vez. |
| within_researcher_variation.csv | within_range | Máximo−mínimo dentro del investigador; NA con menos de dos contextos definidos. |
| within_researcher_variation.csv | within_sample_sd | Desviación estándar muestral de contextos definidos; NA con menos de dos. |
| within_researcher_variation.csv | last_minus_first | Último−primer valor anual definido; no supone continuidad ni efecto causal. |
| within_researcher_variation.csv | variation_status | varies si rango>1e−10 con al menos dos valores; constant si rango≤tolerancia; insuficiente si menos de dos. |
| within_researcher_variation.csv | first_defined_year | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| within_researcher_variation.csv | last_defined_year | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| within_researcher_variation_summary.csv | scope | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| within_researcher_variation_summary.csv | indicator | Etiqueta del universo, indicador o estado descriptivo definido en protocolo/README. |
| within_researcher_variation_summary.csv | researchers_total | Número de investigadores que cumplen la condición indicada; las categorías de una misma clasificación son excluyentes. |
| within_researcher_variation_summary.csv | researchers_with_any_context | Número de investigadores que cumplen la condición indicada; las categorías de una misma clasificación son excluyentes. |
| within_researcher_variation_summary.csv | researchers_two_or_more_defined | Número de investigadores que cumplen la condición indicada; las categorías de una misma clasificación son excluyentes. |
| within_researcher_variation_summary.csv | researchers_with_variation | Número de investigadores que cumplen la condición indicada; las categorías de una misma clasificación son excluyentes. |
| within_researcher_variation_summary.csv | researchers_constant | Número de investigadores que cumplen la condición indicada; las categorías de una misma clasificación son excluyentes. |
| within_researcher_variation_summary.csv | researchers_less_than_two_defined | Número de investigadores que cumplen la condición indicada; las categorías de una misma clasificación son excluyentes. |
| within_researcher_variation_summary.csv | median_within_range | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |
| within_researcher_variation_summary.csv | median_within_sd | Campo auxiliar documentado por su fórmula/construcción en el código reproducible y el protocolo; se conserva sin imputar faltantes. |