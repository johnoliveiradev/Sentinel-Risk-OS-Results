# Roadmap

## Phase 1: Results-only (current)
- Publish HTML reports, CSV exports, derived metrics, and charts.
- Provide verification scripts that operate solely on published data.
- Maintain strict blackbox posture—no engine code or parameters.

## Phase 2: Audit harness
- Add automated checks to compare new runs against historical ranges.
- Introduce baseline benchmarks (kept public) for regression detection.
- Expand schema validation to cover additional outputs.

## Phase 3: Partial open core
- Expose non-sensitive components such as data loaders or visualization templates.
- Enable community-contributed analyses built on top of the published outputs.
- Keep proprietary inference and scoring logic private while broadening transparency.
