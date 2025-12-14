# Sentinel Risk OS — FAQ

This FAQ addresses common questions about the **Sentinel Risk OS Results** repository,
its scope, and how the published outputs should be interpreted.

---

## What is Sentinel Risk OS?

Sentinel Risk OS is a **private, deterministic engine** designed to detect
**structural risk regimes** and **stress accumulation** in time-series systems.

This repository publishes **results only** — reports, CSV exports, and derived
summaries — without exposing proprietary internals.

---

## Is the engine open source?

No.

The engine is intentionally kept **private**.

This repository exists to publish **observable outputs** and allow independent
inspection of their structure and consistency, not to share implementation details.

---

## What problem does Sentinel Risk OS solve?

Most risk tools answer:

> *“How stressed is the system right now?”*

Sentinel Risk OS answers:

> *“What structural phase is the system in, how did stress form, how long did it
persist, and how did it transition?”*

It operates at the **regime level**, not at the signal or prediction level.

---

## Is this a trading or prediction system?

No.

Sentinel Risk OS:
- does not generate trade signals
- does not forecast prices
- does not optimize returns
- does not provide entry/exit recommendations

Its purpose is **structural risk interpretation**, not trading execution.

---

## How is this different from VIX, OFR Financial Stress Index, or similar indicators?

Indices such as VIX or OFR FSI provide **scalar measurements of stress intensity**
at a given point in time.

Sentinel Risk OS:
- detects **regimes**
- aggregates behavior into **coherent stress windows**
- identifies **onset, persistence, peak, and transition**

The approaches are **complementary**, but not interchangeable.

---

## Is Sentinel just another index with labels applied?

No.

Regimes and windows in Sentinel Risk OS are **constructed structural objects**, not
thresholds applied to a continuous index.

The system explicitly models **temporal persistence and transitions**, which scalar
indices do not.

---

## Can the same results be obtained by thresholding existing indices?

No.

Thresholding an index:
- introduces arbitrary cutoffs
- fragments continuous behavior
- removes temporal coherence

Sentinel windows are formed through **structural aggregation**, not post-hoc filtering.

---

## Does Sentinel Risk OS use machine learning?

The published results do not depend on:
- supervised learning
- probabilistic modeling
- neural networks

The internal engine architecture is not disclosed.

---

## Are the results reproducible?

The **engine outputs are not reproducible** without access to the private system.

However:
- all **derived metrics**
- all **figures**
- all **run summaries**

can be regenerated deterministically from the published CSVs using the provided
verification scripts.

---

## Why publish results without the model?

This repository follows a **results-first validation model**.

The goal is to allow independent inspection of:
- observable behavior
- regime structure
- temporal consistency
- cross-asset coherence

without requiring access to proprietary internals.

This mirrors how advanced research systems are often evaluated:
**evidence before explanation**.

---

## What do the regime labels mean?

- **Stable** — structurally normal conditions  
- **Pre-Stress** — early structural deviation  
- **Core Stress** — sustained stress accumulation  
- **Extreme** — high-intensity structural instability  

Regimes describe **structural phases**, not predictions or outcomes.

---

## Are regime labels asset-specific?

No.

Regime labels are **structural abstractions** and are applied consistently across
assets.

This allows cross-asset comparison without redefining semantics per market.

---

## Why focus on daily resolution?

Daily resolution provides a balance between:
- noise reduction
- structural persistence
- interpretability

The system is designed to capture **regime-level behavior**, not intraday dynamics.

---

## Does Sentinel Risk OS generalize beyond financial markets?

The engine is designed around **structural detection principles**, not asset-specific
heuristics.

This repository, however, is intentionally scoped to **financial time-series results**
only.

---

## Is Sentinel Risk OS intended to replace existing risk tools?

No.

Sentinel Risk OS can be used:
- alongside traditional indicators
- as a higher-level structural layer
- as a contextual framework for interpretation

It does not aim to replace monitoring or reporting tools.

---

## What should I look for when reviewing the reports?

Focus on:
- duration of stress windows
- internal peak timing
- regime transitions
- persistence versus transience

The value lies in **structure**, not isolated values.

---

## Where can I find the latest reports?

Published reports are available via GitHub Pages:

https://johnoliveiradev.github.io/Sentinel-Risk-OS-Results/

---

## What is the long-term roadmap?

The current phase focuses on:
- single-asset analysis
- daily resolution
- public, verifiable outputs

Future phases may include:
- cross-asset interaction
- extended validation
- external audit frameworks

Details will be published only when appropriate.

---

## Final note

This repository exists to publish **what the system observes**, not **how it works**.

Interpret the outputs as **structural evidence**, not forecasts.

*Evidence before explanation.*
