Sentinel Risk OS — Published Results

This repository publishes verified outputs from Sentinel Risk OS, a private structural risk detection engine.

The engine itself is intentionally not included.

Only results, artifacts, and reproducible metrics are published here to enable independent inspection of observed behavior without exposing proprietary logic.

Why This Matters

Most risk systems react after instability becomes obvious.

Sentinel Risk OS focuses on early detection of structural regime transitions, providing visibility into stress accumulation before it manifests as full market dislocation.

The value of this repository is not prediction accuracy, but observable structural behavior across time and assets.

What Is Included

Static HTML reports for each published run

CSV exports: regime_series.csv, windows.csv

Derived run summaries: run_card.md, run_card.json

Figures regenerated from the published CSVs

Reproducibility helpers to validate metrics and charts

All derived artifacts can be recomputed using only files published in this repository.

What Is Not Included

Sentinel Risk OS engine code

Internal heuristics or parameters

Interval boundaries, nonces, or optimization logic

Trading strategies or predictive models

This repository is results-only by design.

Blackbox Policy

No proprietary engine logic is present

All metrics and figures are derived solely from the exported CSVs

Unknown or new regime labels are surfaced transparently in counts and percentages

The repository enables inspection of outputs and behavior, not internal mechanics

How to Navigate the Results

Results are organized by asset and run timestamp:

runs/
  single/
    {ASSET}/
      {RUN_ID}/


Each run folder contains:

report.html — full visual report

regime_series.csv — daily regime classification

windows.csv — aggregated stress windows

run_card.md / run_card.json — summary and metadata

figures/ — charts regenerated from CSVs

How to View the Reports

Latest published run for ^GSPC:

runs/single/^GSPC/2025-12-13_202058/report.html

GitHub Pages (when configured to use the docs/ folder) serves reports under:

/assets/reports/single/{ASSET}/{RUN_ID}/report.html


Example:

/assets/reports/single/^GSPC/2025-12-13_202058/report.html

Validate the Published Outputs

Install dependencies:

python -m pip install -r repro/environment.txt

Run verification:

python repro/verify_run.py runs/single/^GSPC/2025-12-13_202058

The script recomputes summary metrics and figures and fails fast if schemas or results diverge from expectations.

Repository Structure

docs/ — public documentation and HTML reports for GitHub Pages

runs/ — published results organized by asset and run id

baselines/ — placeholder for future public baselines

repro/ — scripts used to validate and regenerate derived artifacts

Research Philosophy

Sentinel Risk OS follows a results-first publication model.

Evidence precedes explanation.

If the outputs demonstrate consistent structural behavior, further discussion becomes meaningful.

License

MIT License (see LICENSE).
