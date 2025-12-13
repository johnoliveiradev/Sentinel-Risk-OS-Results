# Sentinel Risk OS Results

Public, results-only repository publishing Sentinel Risk OS outputs for transparency without exposing the proprietary engine. This repo contains static reports, CSV exports, derived metrics, and reproducibility helpers so others can verify what was observed from the blackbox engine. No engine code or private parameters are included.

## What is here
- Published HTML report and CSV exports for run `2025-12-13_202058` on asset `^GSPC`.
- Derived run card (Markdown + JSON) summarizing the run.
- Matplotlib figures regenerated from the CSVs only; to keep the repo free of binaries, figures are generated locally and gitignored.
- Reproducibility scripts (`repro/verify_run.py`) to recompute metrics and charts from the published artifacts.

## Blackbox policy
- No proprietary engine logic, intervals, or hidden parameters are present.
- All metrics are recomputed solely from the exported CSVs.
- Any unknown regime labels are surfaced transparently in counts/percentages.

## How to view the report
- Latest HTML report: [``](runs/single/).
- GitHub Pages can serve from the `docs/` folder; configure Pages to point to `docs` and the report will be available at `/assets/reports/single/^GSPC/2025-12-13_202058/report.html`.

## Validate the published outputs
1. Install dependencies: `python -m pip install -r repro/environment.txt`.
2. Run verification: `python repro/verify_run.py runs/single/^GSPC/2025-12-13_202058`.
3. The script will regenerate `run_card.json`, `run_card.md`, and figures, failing fast if schemas differ from expectations.

## Repository layout
- `docs/` — public documentation, including a copy of the HTML report for Pages.
- `runs/` — published results organized by asset and run id.
- `baselines/` — placeholder for future public baselines.
- `repro/` — scripts used to validate and regenerate derived artifacts.

## License
MIT License (see `LICENSE`).
