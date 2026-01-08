# Student Workflow & Submission Guide

> [!IMPORTANT]
> **READ THIS FIRST**: Do not commit directly to the `main` branch of this repository.

This repository serves as the **template** for your project. To work on it, follow the standard GitHub workflow:

1.  **Fork** this repository to your own GitHub account (click the "Fork" button in the top right).
2.  **Clone** your forked repository to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/evidence-in-motion.git
    ```
3.  **Create a Branch** for your work. **Do not work on `main`**.
    ```bash
    git checkout -b feature/initial-setup
    ```
4.  **Work and Commit** your changes locally.
5.  **Push** your branch to your fork:
    ```bash
    git push -u origin feature/initial-setup
    ```
6.  **Open a Pull Request (PR)** on GitHub to merge your changes into your `main` branch (or submit as directed by your instructor).

---

# Evidence in Motion Project

## Project Overview
This repository contains the "Evidence in Motion" project, designed to turn raw data into validated, documented data and produce an auditable report.

## Problem Statement

Students should pick **one dataset/problem** and commit to it early.

### Option A — Public dataset cleanup + reporting
- **Context**: Choose a public dataset with known quality issues (missing values, inconsistent types, duplicates, messy categories).
- **Goal**: Deliver a cleaned dataset + a short report with 2–3 concrete insights.

### Option B — Multi-source merge
- **Context**: Combine two related datasets (e.g., demographics + outcomes).
- **Goal**: Deliver a merged dataset with a documented join strategy and coverage analysis.

### Option C — Time-series “refresh” pipeline
- **Context**: Simulate regular updates (weekly/monthly file drops).
- **Goal**: Pipeline supports reruns and produces consistent outputs.

## How to Run

### 1. Local Setup
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the pipeline:
    ```bash
    python src/run_pipeline.py
    ```
3.  Run tests manually:
    ```bash
    pytest
    ```

### 2. Automated Validation (CI/CD)
Every time you push a commit or open a Pull Request, **GitHub Actions** will automatically run the tests (`pytest`).

-   **✅ Pass**: Your code meets the quality standards. This is required for `v0.1` and `v1.0` releases.
-   **❌ Fail**: Something is broken. Check the "Actions" tab or the PR details to see which test failed.

**Note**: The history of your CI runs serves as **evidence** of your iterative progress and data quality discipline. Do not delete failing runs; they are part of the audit trail.

## Outputs
- Cleaned dataset in `data/processed/`
- Summary stats

## Project Structure
```
.
├── README.md
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── docs/
│   ├── data-dictionary.md
│   └── report.md
├── notebooks/
├── src/
│   ├── ingest.py
│   ├── transform.py
│   ├── validate.py
│   └── run_pipeline.py
├── tests/
│   ├── test_schema.py
│   ├── test_quality_rules.py
│   └── test_pipeline_runs.py
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml
```
