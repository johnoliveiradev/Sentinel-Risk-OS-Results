# Methodology

This repository publishes the observable outputs from Sentinel Risk OS without revealing the engine itself. The engine is treated as a blackbox: only the HTML report and CSV exports are shared, and every derived artifact in this repo is computed from those exports using open-source tools (pandas, matplotlib, Python standard library).

## Regime definitions
The engine emits categorical regime labels per day and per evaluation window. Typical labels include:
- **Stable** — normal conditions with low stress indicators.
- **Pre-Stress** — early signs of stress accumulation.
- **Core Stress** — pronounced stress conditions.
- **Extreme** — tail-risk or crisis states.

Additional labels may appear; they are preserved verbatim in summaries.

## Files published per run
- `report.html` — static backtest report as produced by the engine.
- `regime_series.csv` — per-day regime assignments (and optional scores) across the backtest horizon.
- `windows.csv` — window-level evaluations with start/end/peak dates, regime tags, and `score_max` values.
- `run_card.json` / `run_card.md` — derived summaries computed from the CSVs only.
- `figures/*.png` — visualizations regenerated from CSV data.

## How metrics are derived
1. CSV schemas are validated to ensure expected columns exist.
2. Regime counts and percentages are computed directly from `regime_series.csv`.
3. Window statistics (counts, duration summaries, score summaries) are computed from `windows.csv` grouped by regime.
4. Charts are rendered with matplotlib using only the published data. If a daily score series is absent, window-level scores are used to reconstruct a stepwise "best score so far" view.

The process is deterministic and reproducible with `python repro/verify_run.py runs/single/^GSPC/2025-12-13_202058`.
