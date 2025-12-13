from __future__ import annotations

import argparse
from pathlib import Path

from compute_summary import (
    build_summary,
    generate_figures,
    save_json,
    write_run_card_md,
)


RUN_ID = "2025-12-13_202058"
ASSET = "^GSPC"


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate run artifacts from published CSVs")
    parser.add_argument(
        "run_dir",
        nargs="?",
        default=Path("runs") / "single" / ASSET / RUN_ID,
        type=Path,
        help="Path to the run directory containing regime_series.csv and windows.csv",
    )
    args = parser.parse_args()
    run_dir: Path = args.run_dir

    regime_path = run_dir / "regime_series.csv"
    windows_path = run_dir / "windows.csv"
    figures_dir = run_dir / "figures"

    if not regime_path.exists():
        raise FileNotFoundError(f"Missing regime_series.csv at {regime_path}")
    if not windows_path.exists():
        raise FileNotFoundError(f"Missing windows.csv at {windows_path}")

    summary_obj, summary_dict = build_summary(ASSET, RUN_ID, regime_path, windows_path)

    # Persist summaries
    save_json(summary_dict, run_dir / "run_card.json")
    write_run_card_md(summary_dict, run_dir / "run_card.md")

    # Generate figures
    generate_figures(summary_obj.regime_series, summary_obj.windows, figures_dir)

    print("Run card generated at", run_dir / "run_card.json")
    print("Figures written to", figures_dir)
    print("Summary:")
    print(summary_dict)


if __name__ == "__main__":
    main()
