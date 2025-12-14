# Sentinel Risk OS — Published Results

This repository publishes **verified outputs** from **Sentinel Risk OS**, a private
structural risk detection engine.

The engine itself is intentionally **not included**.

Only results, artifacts, and reproducible metrics are published here to enable
independent inspection of observed behavior **without exposing proprietary logic**.

---

## Why This Matters

Most risk systems react **after** instability becomes obvious.

Sentinel Risk OS focuses on **early detection of structural regime transitions**,
providing visibility into stress accumulation before it manifests as full market
dislocation.

The value of this repository is **not prediction accuracy**, but:

- Structural awareness  
- Regime persistence  
- Cross-asset consistency  

---

## What Is Included

This repository contains **only public, non-proprietary artifacts**:

- Static HTML reports for each published run  
- CSV exports (`regime_series.csv`, `windows.csv`)  
- Derived run summaries (`run_card.md`, `run_card.json`)  
- Figures regenerated exclusively from the published CSVs  
- Reproducibility helpers to validate metrics and charts  

All derived artifacts can be recomputed using **only** the files published here.

---

## What Is Not Included

- Sentinel Risk OS engine code  
- Internal heuristics or parameters  
- Interval boundaries, nonces, or optimization logic  
- Trading strategies or predictive models  

This repository is **results-only by design**.

---

## Blackbox Policy

- No proprietary engine logic is present  
- All metrics and figures are derived solely from exported CSVs  
- Unknown regime labels are surfaced transparently  
- The repository allows inspection of **outputs and behavior**, not internals  

---

## How to Navigate the Results

Results are organized by asset and run timestamp:

```text
runs/
└── single/
    └── ASSET/
        └── RUN_ID/
Each run folder contains:

report.html — full visual report

regime_series.csv — daily regime classification

windows.csv — aggregated stress windows

run_card.md / run_card.json — summary and metadata

figures/ — charts regenerated from CSVs

How to View the Reports
Latest published run for S&P 500 (^GSPC):

text
Copiar código
runs/single/^GSPC/2025-12-13_202058/report.html
HTML reports are also served via GitHub Pages.

When Pages is configured to use the docs/ folder, reports are available at:


/assets/reports/single/ASSET/RUN_ID/report.html
Example:


/assets/reports/single/^GSPC/2025-12-13_202058/report.html
Validate the Published Outputs
All derived artifacts can be regenerated locally from the published CSVs.

Install dependencies
bash
Copiar código
python -m pip install -r repro/environment.txt
Run verification
bash

python repro/verify_run.py runs/single/^GSPC/2025-12-13_202058
The script recomputes summary metrics and figures and fails fast if schemas
or results diverge from expectations.

Repository Structure
docs/ — public documentation and HTML reports for GitHub Pages

runs/ — published results organized by asset and run id

baselines/ — placeholder for future public baselines

repro/ — scripts used to validate and regenerate derived artifacts

Research Philosophy
Sentinel Risk OS follows a results-first publication model.

Evidence precedes explanation.

If the outputs demonstrate consistent structural behavior,
further discussion becomes meaningful.

License
MIT License (see LICENSE).
