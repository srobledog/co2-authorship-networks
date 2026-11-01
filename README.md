# CO2 networking — reproducibility package v0.1

Prepared for author review. This repository reproduces the frozen exploratory CO2 results from the final analytical samples. It does not establish inferential validity or confirm/refute H1/H2.

## Quick start

Tested with Python 3.12 (see `results/reproduction_report.json` for the exact version) and the exact package versions in `requirements.txt`. Run from this directory:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/reproduce.py
```

On Windows use `.venv\Scripts\activate`. Installation requires access to Python package repositories. The analysis itself requires no network, API keys, original workstation paths, or live bibliographic services. Allow several minutes. The command fails on a failed comparison and writes machine-readable checks to `results/reproduction_report.json`. It overwrites generated `results/` files only; frozen samples and reference files remain unchanged.

## Contents

- `data/`: three frozen analytical samples and inherited dictionaries, including uncertainty flags.
- `reference/`: original fitted parameters, diagnostics, endpoints, and manuscript point-only tables.
- `vendor/fit_models.py`: original fitting code, unchanged; imported by the controlled runner.
- `vendor/predict_points.py`: original prediction function extracted verbatim, excluding the bootstrap execution block.
- `scripts/reproduce.py`: checks hashes, refits the original nine models, recalculates point summaries and predictions, and compares outputs.
- `scripts/build_tables.py`: original table/figure builder with its root redirected to the generated staging directory. No changes to statistical formulas.
- `documentation/`: frozen specification, indicator formulas, closure note and inference audit reports.
- `results/`: observed reproduction evidence, refitted parameters, tables and figures.
- `MANIFEST.sha256`: release file integrity checks.

## Statistical scope

The principal sample contains 1,079 researcher–publication observations, 292 researchers, 717 researcher–year contexts and 765 publications through 2025. The quality sensitivity contains 791 observations; inclusion of 2026 contains 1,080. Researchers may appear on multiple papers and papers may include multiple eligible researchers.

M0, H1 and H2 are the frozen researcher-random-intercept logistic working models. H1 includes density-by-prior-authorship interactions; H2 separately includes weighted constraint. Prior histories use years t−3 through t−1; mixed histories remain a separate category. Higher constraint is greater restriction, not greater brokerage. See the specification and dictionaries for controls, scaling and reference categories.

Each of nine refits uses the original three starting values and 60-node Gauss–Hermite integration; 100-node fits check numerical stability. Standardized predictions use the original 100-node integration over a new researcher intercept. These are GLMM predictions, not a separately fitted marginal model. Output includes no confidence intervals, standard errors or hypothesis tests. The extracted prediction function has no resampling execution path. Never use the historical bootstrap intervals to evaluate H1/H2.

## Reproduction checks

Before running, absolute comparison tolerances were set to 1e-4 for the full parameter vector (including log sigma), 1e-6 for log likelihood, 1e-5 for generated model-summary tables/predictions, and 1e-12 for descriptive table values. These are numerical agreement criteria, not statistical uncertainty. The original 0.01 thresholds for the 100-node integration check are retained. CSV comparisons check both labels and values. Graphics are regenerated from checked numerical sources; image bytes are not expected to match across rendering environments.

The tested environment used already installed dependencies matching the pinned versions. A fresh package installation on another operating system was not tested. See `REPRODUCTION_REPORT.md` for observed results and limitations.

## Boundaries

This release starts at frozen analytical samples. It does **not** independently reproduce the initial Scopus/WoS search, BibFusion enrichment, identity corrections, temporal network reconstruction, indicator derivation, or sample selection from raw records. Formula and audit documentation is included, but executable upstream inputs and scripts must be consolidated separately before claiming end-to-end reproducibility. The support graph used in constraint normalization is not reconstructed here.

No new hypotheses, alternative model specifications, marginal logistic fits, jackknife runs, bootstrap runs, or calibration simulations are executed. Historical inferential audits are included as documentation, not an active pipeline. Reproduction of a model cannot resolve its uncertain dependence assumptions, incomplete histories, selection through references/the giant component, or the limitations of authorship position as an indicator.

## Release and citation decisions

This package is hosted in the private author-review repository https://github.com/srobledog/co2-authorship-networks. The owner explicitly authorized uploading the three researcher-level analytical samples. Public-release permissions for the derived bibliographic tables and code license remain to be agreed by the authors. Data contain bibliographic identifiers and author names; they are not anonymized. No open license is asserted by this package. Review redistribution terms before public release; raw subscription-database exports are not bundled.

Before public release: supply the definitive author list, article title, license decisions and archived release DOI; then add a complete `CITATION.cff` and data/code availability statement. No DOI or authorship metadata has been invented.
