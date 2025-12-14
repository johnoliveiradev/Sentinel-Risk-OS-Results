# Sentinel Risk OS — Single-Asset Backtest
**Asset:** ^GSPC
**Run ID:** 2025-12-14_154807
**Period:** 2025-06-10 → 2025-12-12 (130 days)

## Regime Distribution
- Stable: 77 days (59.23%)
- Attention: 30 days (23.08%)
- Elevated Risk: 23 days (17.69%)

## Windows
- Total windows: 12
- By regime:
  - Pre-Stress: 8
  - Core Stress: 4
- Top windows by max score:
  - 2025-11-13 00:00:00 → 2025-12-05 00:00:00 | Core Stress | score=3.25 | peak=2025-11-20 00:00:00
  - 2025-11-04 00:00:00 → 2025-11-07 00:00:00 | Core Stress | score=2.70 | peak=2025-11-06 00:00:00
  - 2025-10-20 00:00:00 → 2025-11-04 00:00:00 | Pre-Stress | score=2.46 | peak=2025-11-04 00:00:00
  - 2025-10-15 00:00:00 → 2025-10-16 00:00:00 | Pre-Stress | score=2.34 | peak=2025-10-16 00:00:00
  - 2025-10-16 00:00:00 → 2025-10-20 00:00:00 | Core Stress | score=2.34 | peak=2025-10-16 00:00:00
- Duration (days) by regime:
  - Core Stress: min=3.0, median=4.5, max=22.0
  - Pre-Stress: min=1.0, median=4.5, max=15.0
- Max score by regime:
  - Core Stress: min=2.33, median=2.52, max=3.25
  - Pre-Stress: min=1.01, median=1.82, max=2.46

## Metadata
- start_date: 2024-12-14
- end_date: 2025-12-14
- n_days: 249
- code_version: None
- environment: 3.13.5
- machine: Windows-10-10.0.19045-SP0
