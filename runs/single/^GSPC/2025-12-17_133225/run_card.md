# Sentinel Risk OS — Single-Asset Backtest
**Asset:** ^GSPC
**Run ID:** 2025-12-17_133225
**Period:** 2025-06-11 → 2025-12-16 (131 days)

## Regime Distribution
- Stable: 74 days (56.49%)
- Attention: 47 days (35.88%)
- Elevated Risk: 10 days (7.63%)

## Windows
- Total windows: 11
- By regime:
  - Pre-Stress: 8
  - Core Stress: 3
- Top windows by max score:
  - 2025-11-18 00:00:00 → 2025-11-28 00:00:00 | Core Stress | score=3.25 | peak=2025-11-20 00:00:00
  - 2025-10-09 00:00:00 → 2025-11-06 00:00:00 | Pre-Stress | score=2.70 | peak=2025-11-06 00:00:00
  - 2025-11-06 00:00:00 → 2025-11-07 00:00:00 | Core Stress | score=2.70 | peak=2025-11-06 00:00:00
  - 2025-12-01 00:00:00 → 2025-12-03 00:00:00 | Core Stress | score=2.65 | peak=2025-12-01 00:00:00
  - 2025-11-28 00:00:00 → 2025-12-01 00:00:00 | Pre-Stress | score=2.65 | peak=2025-12-01 00:00:00
- Duration (days) by regime:
  - Core Stress: min=1.0, median=2.0, max=10.0
  - Pre-Stress: min=1.0, median=5.5, max=28.0
- Max score by regime:
  - Core Stress: min=2.65, median=2.70, max=3.25
  - Pre-Stress: min=1.02, median=1.89, max=2.70

## Metadata
- start_date: 2024-12-17
- end_date: 2025-12-17
- n_days: 250
- code_version: None
- environment: 3.13.5
- machine: Windows-10-10.0.19045-SP0
