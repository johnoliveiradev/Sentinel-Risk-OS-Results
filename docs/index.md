# Sentinel Risk OS — Published Reports

This site publishes **verified, results-only outputs** from **Sentinel Risk OS**,  
a private, deterministic engine for **structural risk regime detection**.

The engine itself is intentionally not included.

All materials here are derived exclusively from exported artifacts
(HTML reports, CSVs, and reproducible metrics) to allow independent inspection
of observed behavior without exposing proprietary internals.

---

## Latest Reports

### Equity Indices

- **S&P 500 (^GSPC)**  
  Run ID: `2025-12-13_215324`  
  → [View report](assets/reports/single/%5EGSPC/2025-12-13_215324/report.html)

- **S&P 500 (^SPX)**  
  Run ID: `2025-12-13_224144`  
  → [View report](assets/reports/single/%5ESPX/2025-12-13_224144/report.html)

---

### Crypto Assets

- **Bitcoin (BTC-USD)**  
  Run ID: `2025-12-13_224144`  
  → [View report](assets/reports/single/BTC-USD/2025-12-13_224144/report.html)

---

## How to Read These Reports

Sentinel Risk OS operates at the **regime level**, not at the signal or prediction level.

Key concepts:

- **Stable** — structurally normal conditions  
- **Pre-Stress** — early structural deviation  
- **Core Stress** — sustained stress accumulation  
- **Extreme** — high-intensity structural instability  

Reports aggregate daily behavior into **coherent stress windows** with:
- start and end dates
- duration
- internal peak date
- maximum stress score
- post-window regime transitions

This framing focuses on **how risk forms, persists, and dissolves over time**.

---

## Reproducibility & Transparency

For each run, the repository provides:

- Original HTML report
- Exported CSVs (`regime_series`, `windows`)
- Derived summaries (`run_card.md`, `run_card.json`)
- Verification scripts to recompute metrics and figures

All derived artifacts are generated **only** from published outputs.

---

## Blackbox Policy

- No engine code is included
- No parameters, heuristics, or internal states are exposed
- No claim of reproducibility of the engine itself

This repository exists to publish **evidence**, not implementation.

---

## Repository

- GitHub: https://github.com/johnoliveiradev/Sentinel-Risk-OS-Results
- License: MIT (applies to published artifacts and documentation only)

---

*Evidence before explanation.*
