# Threat Model

Sentinel Risk OS is a proprietary engine. This repository is designed to publish outputs without leaking implementation details or tunable parameters.

## What is exposed
- Static HTML reports.
- CSV exports for regimes and evaluation windows.
- Derived summaries and plots computed from those CSVs.

## What is deliberately hidden
- Engine source code, interval logic, and parameterization.
- Any internal identifiers beyond what appears in CSVs.
- Nonces, seeds, or training data.

## Defensive measures
- Reproducibility relies solely on the published CSVs; no secret inputs are required.
- Scripts validate CSV schemas and fail loudly if unexpected columns appear.
- Unknown regimes are handled verbatim, preventing inference of remapped labels.

This approach keeps the engine a blackbox while allowing independent verification of the published outputs.
