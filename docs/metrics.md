# Metrics

All metrics are computed from published CSVs using pandas. No private parameters are inferred.

## Regime series metrics
- **start_date / end_date** — first and last dates in `regime_series.csv`.
- **n_days** — number of daily observations.
- **regime_counts** — counts of each unique regime label.
- **regime_percentages** — percentage share for each regime label over the period.

## Window metrics
- **window_counts_by_regime** — number of windows per regime.
- **top_windows_by_score_max** — top five windows ranked by `score_max` (start_date, end_date, peak_date, regime, score_max).
- **duration_summary_by_regime** — minimum, median, and maximum window length in days per regime.
- **score_max_summary_by_regime** — minimum, median, and maximum `score_max` per regime.

## Charts
- **best_score_so_far.png** — cumulative maximum of daily score when available; otherwise step plot of window `score_max` by end date. If neither is present, a placeholder chart is generated.
- **regime_distribution.png** — bar chart of regime percentages.
- **window_timeline.png** — Gantt-like visualization of windows by regime.
- **window_score_ranking.png** — top 10 windows by `score_max` as a horizontal bar chart.
