### Project overview

In many real settings, the hardest part is not “running analysis”, but turning messy, inconsistent inputs into a trustworthy dataset and a clear evidence trail.

This project asks students to build a repository that:

- turns **raw data → validated, documented data**
- produces an **auditable report** (findings + limitations)
- demonstrates **production habits** (tests, reproducibility, versioning)

### Nexus alignment

- **Primary domains:** Data Engineering, Adaptive Infrastructure
- **Secondary domains:** Systems Thinking, Computational Logic

### Student-facing learning outcomes

By the end, students should be able to:

- design a simple data pipeline with clear stages and outputs
- validate data quality with automated checks
- document decisions (assumptions, transformations, limitations)
- ship a repo that another person can run end-to-end

---

### Problem statement (choose one)

Students should pick **one dataset/problem** and commit to it early.

**Option A — Public dataset cleanup + reporting**

- Choose a public dataset with known quality issues (missing values, inconsistent types, duplicates, messy categories).
- Goal: deliver a cleaned dataset + a short report with 2–3 concrete insights.

**Option B — Multi-source merge**

- Combine two related datasets (e.g., demographics + outcomes).
- Goal: deliver a merged dataset with a documented join strategy and coverage analysis.

**Option C — Time-series “refresh” pipeline**

- Simulate regular updates (weekly/monthly file drops).
- Goal: pipeline supports reruns and produces consistent outputs.

### Definition of done (MVP)

A repo is “done” when:

- a new contributor can run it end-to-end using the README
- raw inputs are preserved and outputs are reproducible
- quality checks fail loudly when assumptions break
- evidence artifacts are clear enough for review

---

### Deliverables (evidence artifacts)

**Required**

- [`README.md`](http://README.md)
    - what the dataset is
    - what problem is being solved
    - how to run
    - what outputs are produced
- `docs/[data-dictionary.md](http://data-dictionary.md)`
    - schema, field meanings, units
    - missing value policy
- `docs/[report.md](http://report.md)`
    - findings (2–3)
    - methods summary
    - limitations
    - next steps
- Pipeline code (`src/`) that produces:
    - cleaned dataset in `data/processed/`
    - summary stats / QA report
- Tests (`tests/`) for:
    - schema validation
    - row/column constraints
    - basic sanity checks

**Recommended**

- `notebooks/` or `reports/` for exploratory work, but keep the pipeline runnable without notebooks.

---

### GitHub workflow requirements (graded behaviors)

- **Issues**
    - at least 5 issues, each with acceptance criteria
    - include at least 1 issue tagged `data-quality`
- **Pull Requests**
    - at least 2 PRs
    - each PR includes: summary, testing notes, and what changed in outputs
- **Releases / tags**
    - `v0.1` = pipeline runs end-to-end
    - `v1.0` = evidence package complete (report + dictionary + tests)

---

### Suggested repo structure (complete)

```
.
├── [README.md](http://README.md)
├── data/
│   ├── raw/
│   ├── interim/                  # optional
│   └── processed/
├── docs/
│   ├── [data-dictionary.md](http://data-dictionary.md)
│   └── [report.md](http://report.md)
├── notebooks/                    # optional
├── src/
│   ├── [ingest.py](http://ingest.py)
│   ├── [transform.py](http://transform.py)
│   ├── [validate.py](http://validate.py)
│   └── run_[pipeline.py](http://pipeline.py)
├── tests/
│   ├── test_[schema.py](http://schema.py)
│   ├── test_quality_[rules.py](http://rules.py)
│   └── test_pipeline_[runs.py](http://runs.py)
├── requirements.txt              # or environment.yml
├── .gitignore
└── .github/
    └── workflows/
        └── ci.yml                # run tests on PR
```

---

### Evaluation rubric (simple)

- **Reproducibility (25%)**: can another person run it and get the same outputs?
- **Data quality discipline (25%)**: are checks explicit and automated?
- **Documentation & audit trail (25%)**: assumptions, transformations, limitations are clear.
- **Evidence package (25%)**: report + dictionary + outputs are coherent and credible.

---

### Stretch goals

- Add GitHub Actions CI to run tests.
- Add a “data drift” check (row counts, schema drift, category changes).
- Add a single command runner (`make run` or `python -m [src.run](http://src.run)_pipeline`).
- Add a small [`CHANGELOG.md`](http://CHANGELOG.md) describing major pipeline decisions.