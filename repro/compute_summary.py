from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, date
from pathlib import Path
from statistics import median
from typing import Dict, List, Tuple
import zlib
import struct

# Utility: simple PNG writer using RGB tuples

def _write_png(width: int, height: int, pixels: List[List[Tuple[int, int, int]]], path: Path) -> None:
    raw_data = b"".join(b"".join(struct.pack("BBB", *pixel) for pixel in row) for row in pixels)
    # Add filter bytes per row (0 for none)
    scanlines = b"".join(b"\x00" + raw_data[i * width * 3 : (i + 1) * width * 3] for i in range(height))
    compressed = zlib.compress(scanlines)

    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    header = chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    idat = chunk(b"IDAT", compressed)
    iend = chunk(b"IEND", b"")
    png_bytes = b"\x89PNG\r\n\x1a\n" + header + idat + iend
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png_bytes)


# Simple text rendering using a 5x7 pixel font
_FONT = {
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    "-": ["00000", "00000", "11111", "00000", "00000", "00000", "00000"],
}

for idx, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:/^_"):
    # crude font: diagonal pattern for letters/numbers if not explicitly defined
    pattern = []
    for row in range(7):
        row_bits = ["1" if (row + i) % 2 == 0 else "0" for i in range(5)]
        pattern.append("".join(row_bits))
    _FONT[ch] = pattern


def _render_text_line(text: str) -> List[List[Tuple[int, int, int]]]:
    scale = 2
    spacing = 1
    rows = [[(255, 255, 255)]]  # start with 1x1 white padding row
    glyph_rows = 7 * scale
    row_data = [[(255, 255, 255)] for _ in range(glyph_rows)]
    for char in text.upper():
        glyph = _FONT.get(char, _FONT[" "])
        for r in range(7):
            pixels = [(0, 0, 0) if bit == "1" else (255, 255, 255) for bit in glyph[r]]
            expanded = []
            for px in pixels:
                expanded.extend([px] * scale)
            for s in range(scale):
                row_data[r * scale + s].extend(expanded + [(255, 255, 255)] * spacing)
    rows.extend(row_data)
    rows.append([(255, 255, 255)] * len(rows[1]))
    return rows


def _render_text_image(text: str, path: Path) -> None:
    pixels = _render_text_line(text)
    width = max(len(r) for r in pixels)
    # Normalize row lengths
    norm_rows: List[List[Tuple[int, int, int]]] = []
    for row in pixels:
        if len(row) < width:
            row = row + [(255, 255, 255)] * (width - len(row))
        norm_rows.append(row)
    _write_png(width, len(norm_rows), norm_rows, path)


@dataclass
class RegimeEntry:
    date: date
    regime: str
    score: float | None


@dataclass
class WindowEntry:
    start_date: date
    end_date: date
    peak_date: date
    regime: str
    score_max: float


def _parse_date(value: str) -> date:
    return datetime.fromisoformat(value).date()


class RegimeSeries:
    def __init__(self, entries: List[RegimeEntry]):
        self.entries = entries

    @classmethod
    def load(cls, path: Path) -> "RegimeSeries":
        with path.open() as f:
            reader = csv.DictReader(f)
            missing = {"date", "regime"} - set(reader.fieldnames or [])
            if missing:
                raise ValueError(f"regime_series.csv is missing required columns: {sorted(missing)}")
            entries: List[RegimeEntry] = []
            for row in reader:
                score_val = float(row["score"]) if row.get("score") not in (None, "",) else None
                entries.append(RegimeEntry(date=_parse_date(row["date"]), regime=row["regime"], score=score_val))
        return cls(entries)

    def start_date(self) -> date:
        return min(e.date for e in self.entries)

    def end_date(self) -> date:
        return max(e.date for e in self.entries)

    def regime_counts(self) -> Dict[str, int]:
        return Counter(e.regime for e in self.entries)

    def regime_percentages(self) -> Dict[str, float]:
        counts = self.regime_counts()
        total = len(self.entries)
        return {k: round(v * 100.0 / total, 4) for k, v in counts.items()}

    def best_score_series(self, window_cumulative: List[Tuple[date, float]] | None = None) -> Tuple[List[date], List[float]]:
        scored = [(e.date, e.score) for e in sorted(self.entries, key=lambda e: e.date) if e.score is not None]
        if scored:
            best = []
            running = float("-inf")
            xs: List[date] = []
            ys: List[float] = []
            for dt_val, score in scored:
                running = max(running, score)
                xs.append(dt_val)
                ys.append(running)
            return xs, ys
        if window_cumulative:
            xs, ys = zip(*window_cumulative)
            return list(xs), list(ys)
        return [], []


class Windows:
    def __init__(self, entries: List[WindowEntry]):
        self.entries = entries

    @classmethod
    def load(cls, path: Path) -> "Windows":
        with path.open() as f:
            reader = csv.DictReader(f)
            missing = {"start_date", "end_date", "peak_date", "regime", "score_max"} - set(reader.fieldnames or [])
            if missing:
                raise ValueError(f"windows.csv is missing required columns: {sorted(missing)}")
            entries: List[WindowEntry] = []
            for row in reader:
                entries.append(
                    WindowEntry(
                        start_date=_parse_date(row["start_date"]),
                        end_date=_parse_date(row["end_date"]),
                        peak_date=_parse_date(row["peak_date"]),
                        regime=row["regime"],
                        score_max=float(row["score_max"]),
                    )
                )
        return cls(entries)

    def counts_by_regime(self) -> Dict[str, int]:
        return Counter(w.regime for w in self.entries)

    def duration_summary(self) -> Dict[str, Dict[str, float]]:
        by_regime: Dict[str, List[int]] = defaultdict(list)
        for w in self.entries:
            duration = (w.end_date - w.start_date).days + 1
            by_regime[w.regime].append(duration)
        summary: Dict[str, Dict[str, float]] = {}
        for regime, durations in by_regime.items():
            summary[regime] = {
                "min": float(min(durations)),
                "median": float(median(durations)),
                "max": float(max(durations)),
            }
        return summary

    def score_summary(self) -> Dict[str, Dict[str, float]]:
        by_regime: Dict[str, List[float]] = defaultdict(list)
        for w in self.entries:
            by_regime[w.regime].append(w.score_max)
        summary: Dict[str, Dict[str, float]] = {}
        for regime, scores in by_regime.items():
            summary[regime] = {
                "min": float(min(scores)),
                "median": float(median(scores)),
                "max": float(max(scores)),
            }
        return summary

    def top_windows(self, n: int = 5) -> List[Dict[str, object]]:
        top = sorted(self.entries, key=lambda w: w.score_max, reverse=True)[:n]
        return [
            {
                "start_date": w.start_date.isoformat(),
                "end_date": w.end_date.isoformat(),
                "peak_date": w.peak_date.isoformat(),
                "score_max": float(w.score_max),
                "regime": w.regime,
            }
            for w in top
        ]

    def cumulative_best_scores(self) -> List[Tuple[date, float]]:
        ordered = sorted(self.entries, key=lambda w: w.end_date)
        running = float("-inf")
        points: List[Tuple[date, float]] = []
        for w in ordered:
            running = max(running, w.score_max)
            points.append((w.end_date, running))
        return points


@dataclass
class RunSummary:
    asset: str
    run_id: str
    regime_series: RegimeSeries
    windows: Windows

    def to_dict(self) -> Dict[str, object]:
        counts = self.regime_series.regime_counts()
        percentages = self.regime_series.regime_percentages()
        window_counts = self.windows.counts_by_regime()
        duration_summary = self.windows.duration_summary()
        score_summary = self.windows.score_summary()
        top_windows = self.windows.top_windows()

        return {
            "asset": self.asset,
            "run_id": self.run_id,
            "regime_series": {
                "start_date": self.regime_series.start_date().isoformat(),
                "end_date": self.regime_series.end_date().isoformat(),
                "n_days": int(len(self.regime_series.entries)),
                "regime_counts": counts,
                "regime_percentages": percentages,
            },
            "windows": {
                "counts_by_regime": window_counts,
                "top_windows_by_score_max": top_windows,
                "duration_summary_by_regime": duration_summary,
                "score_max_summary_by_regime": score_summary,
            },
        }


# Simple plotting helpers using manual PNG drawing

def _blank_canvas(width: int, height: int, color: Tuple[int, int, int] = (255, 255, 255)) -> List[List[Tuple[int, int, int]]]:
    return [[color for _ in range(width)] for _ in range(height)]


def _draw_bar_chart(labels: List[str], values: List[float], title: str, path: Path) -> None:
    width, height = 400, 300
    canvas = _blank_canvas(width, height)
    margin = 50
    max_val = max(values) if values else 1
    bar_width = max(1, (width - 2 * margin) // max(1, len(values)))
    for idx, val in enumerate(values):
        bar_height = int((val / max_val) * (height - 2 * margin))
        x0 = margin + idx * bar_width
        y0 = height - margin
        for x in range(x0, x0 + bar_width - 2):
            for y in range(y0 - bar_height, y0):
                canvas[y][x] = (0, 102, 204)
    _render_text_onto_canvas(canvas, title, margin=5)
    _write_png(width, height, canvas, path)


def _draw_horizontal_bar_chart(labels: List[str], values: List[float], title: str, path: Path) -> None:
    width, height = 400, 300
    canvas = _blank_canvas(width, height)
    margin = 50
    max_val = max(values) if values else 1
    bar_height = max(1, (height - 2 * margin) // max(1, len(values)))
    for idx, val in enumerate(values):
        bar_len = int((val / max_val) * (width - 2 * margin))
        y0 = margin + idx * bar_height
        for x in range(margin, margin + bar_len):
            for y in range(y0, y0 + bar_height - 2):
                canvas[y][x] = (255, 140, 0)
    _render_text_onto_canvas(canvas, title, margin=5)
    _write_png(width, height, canvas, path)


def _draw_step_plot(points: List[Tuple[date, float]], title: str, path: Path) -> None:
    width, height = 400, 250
    canvas = _blank_canvas(width, height)
    margin = 40
    if not points:
        _render_text_onto_canvas(canvas, "score series not available", margin=height // 2 - 10)
        _write_png(width, height, canvas, path)
        return
    xs = list(range(len(points)))
    ys = [p[1] for p in points]
    max_y = max(ys) if ys else 1
    prev_x, prev_y = None, None
    for idx, y_val in zip(xs, ys):
        px = margin + int(idx / max(1, len(xs) - 1) * (width - 2 * margin))
        py = height - margin - int(y_val / max_y * (height - 2 * margin))
        if prev_x is not None and prev_y is not None:
            for x in range(prev_x, px + 1):
                canvas[prev_y][x] = (0, 0, 0)
            for y in range(min(prev_y, py), max(prev_y, py) + 1):
                canvas[y][px] = (0, 0, 0)
        prev_x, prev_y = px, py
    _render_text_onto_canvas(canvas, title, margin=5)
    _write_png(width, height, canvas, path)


def _draw_timeline(windows: Windows, title: str, path: Path) -> None:
    width, height = 500, 300
    canvas = _blank_canvas(width, height)
    margin_x = 60
    margin_y = 30
    entries = sorted(windows.entries, key=lambda w: w.start_date)
    if not entries:
        _render_text_onto_canvas(canvas, "no windows", margin=height // 2 - 10)
        _write_png(width, height, canvas, path)
        return
    min_date = min(w.start_date for w in entries)
    max_date = max(w.end_date for w in entries)
    span_days = max((max_date - min_date).days, 1)
    for idx, w in enumerate(entries):
        y = margin_y + idx * max(1, (height - 2 * margin_y) // max(1, len(entries)))
        x_start = margin_x + int((w.start_date - min_date).days / span_days * (width - 2 * margin_x))
        x_end = margin_x + int((w.end_date - min_date).days / span_days * (width - 2 * margin_x))
        for x in range(x_start, max(x_start + 1, x_end)):
            canvas[y][x] = (0, 0, 0)
    _render_text_onto_canvas(canvas, title, margin=5)
    _write_png(width, height, canvas, path)


def _render_text_onto_canvas(canvas: List[List[Tuple[int, int, int]]], text: str, margin: int = 2) -> None:
    text_img = _render_text_line(text)
    for y, row in enumerate(text_img):
        if y + margin >= len(canvas):
            break
        for x, pixel in enumerate(row):
            if x + margin >= len(canvas[0]):
                break
            canvas[y + margin][x + margin] = pixel


def write_run_card_md(summary: Dict[str, object], output_path: Path) -> None:
    regimes = summary["regime_series"]
    windows = summary["windows"]
    lines = [
        f"# Run Card: {summary['asset']} — {summary['run_id']}",
        "",
        "## Regime Series",
        f"- Start date: {regimes['start_date']}",
        f"- End date: {regimes['end_date']}",
        f"- Observations: {regimes['n_days']}",
        "- Regime counts:",
    ]
    for regime, count in regimes["regime_counts"].items():
        pct = regimes["regime_percentages"].get(regime)
        pct_str = f" ({pct:.2f}%)" if pct is not None else ""
        lines.append(f"  - {regime}: {count}{pct_str}")
    lines.append("")
    lines.append("## Windows")
    lines.append("- Counts by regime:")
    for regime, count in windows["counts_by_regime"].items():
        lines.append(f"  - {regime}: {count}")
    lines.append("- Top windows by score_max:")
    for item in windows["top_windows_by_score_max"]:
        lines.append(
            f"  - {item['start_date']} to {item['end_date']} (peak {item['peak_date']}), {item['regime']}: {item['score_max']:.4f}"
        )
    lines.append("- Duration summary (days):")
    for regime, stats in windows["duration_summary_by_regime"].items():
        lines.append(f"  - {regime}: min {stats['min']:.1f}, median {stats['median']:.1f}, max {stats['max']:.1f}")
    lines.append("- score_max summary:")
    for regime, stats in windows["score_max_summary_by_regime"].items():
        lines.append(f"  - {regime}: min {stats['min']:.4f}, median {stats['median']:.4f}, max {stats['max']:.4f}")

    output_path.write_text("\n".join(lines))


def save_json(summary: Dict[str, object], path: Path) -> None:
    path.write_text(json.dumps(summary, indent=2, sort_keys=True))


def generate_figures(regime_series: RegimeSeries, windows: Windows, figures_dir: Path) -> None:
    figures_dir.mkdir(parents=True, exist_ok=True)
    cumulative = windows.cumulative_best_scores()
    xs, ys = regime_series.best_score_series(cumulative)
    _draw_step_plot(list(zip(xs, ys)), "Best score so far", figures_dir / "best_score_so_far.png")
    counts = regime_series.regime_counts()
    _draw_bar_chart(list(counts.keys()), list(counts.values()), "Regime Distribution", figures_dir / "regime_distribution.png")
    _draw_timeline(windows, "Window Timeline", figures_dir / "window_timeline.png")
    sorted_windows = sorted(windows.entries, key=lambda w: w.score_max, reverse=True)[:10]
    _draw_horizontal_bar_chart(
        [str(i + 1) for i in range(len(sorted_windows))],
        [w.score_max for w in sorted_windows],
        "Top Windows by score_max",
        figures_dir / "window_score_ranking.png",
    )


def build_summary(asset: str, run_id: str, regime_path: Path, windows_path: Path) -> Tuple[RunSummary, Dict[str, object]]:
    regime = RegimeSeries.load(regime_path)
    windows = Windows.load(windows_path)
    summary_obj = RunSummary(asset=asset, run_id=run_id, regime_series=regime, windows=windows)
    summary_dict = summary_obj.to_dict()
    return summary_obj, summary_dict
