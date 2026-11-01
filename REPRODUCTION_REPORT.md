# CO2 — Reproduction report v0.1

Status: **PASS for reproduction from frozen analytical samples**.

The nine original GLMM specifications (M0/H1/H2 across three frozen samples) were fitted again from the original three starting values. All parameter vectors exactly matched the archived vectors in this environment. The largest log-likelihood difference was 5.69e-14. The original 100-node quadrature stability checks also passed; the largest coefficient change relative to 60 nodes was below 6.68e-7.

Nine CSV outputs were compared successfully: eight manuscript/supplementary tables and the 378-row figure source. Two figures were regenerated in PNG, PDF and SVG and visually inspected. Descriptive comparisons used absolute tolerance 1e-12; model-derived table comparisons used 1e-5. Figures contain point curves without uncertainty bands.

The original closure inventory's 49 source-file checksums matched before packaging. The runner completed 36 checks covering packaged input integrity, nine model refits, nine table comparisons and six graphic files. Sample-count and within-context consistency assertions also passed in the table builder. The authoritative execution record is `results/reproduction_report.json`, with refitted parameters and diagnostics saved alongside it. The nested builder's `release_checks.json` reports zero fits because that substage only formats results; the top-level runner performed the nine refits.

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, pandas 2.2.3 and Matplotlib 3.10.8, Linux, one numerical-library thread. Dependencies were already installed; a clean dependency installation or another operating system has not been tested.

No new statistical specifications, calibration simulations, bootstrap or jackknife runs were executed. Previously withdrawn intervals were not regenerated or included in manuscript tables. Reproducing numerical estimates does not validate independence assumptions, inferential uncertainty, causal interpretation or H1/H2.

## Remaining work before a public release

1. Consolidate and test upstream reconstruction from the original exports, identity/date corrections, temporal network and indicator inputs. This package starts at analytical samples and does not claim that upstream chain is reproduced.
2. Agree code/data redistribution permissions and licenses. The package contains named bibliographic metadata and is intended for author review.
3. The private repository is https://github.com/srobledog/co2-authorship-networks. Individual-level sample upload was explicitly authorized by the owner. Definitive author metadata and a release citation/DOI remain pending; no citation identifiers were invented.
4. Independently run the documented command after a fresh dependency installation; the current test used the installed matching environment.

Hypotheses and manuscript were not modified. The statistical closure note remains the authority on permitted interpretation.
