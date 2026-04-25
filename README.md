# FinOps Cost-to-Action Pipeline

This project demonstrates how to turn AWS Cost and Usage Report (CUR) data into actionable engineering workflows.

Instead of stopping at cost visibility, this pipeline:
- Ingests CUR data using Python
- Classifies cost signals (baseline, growth, inefficiency)
- Generates Jira-ready action items
- Enables engineers to validate workload behavior before financial commitments (Savings Plans / RIs)

## Why this matters

Most teams struggle with the gap between **cost insight and execution**.

This system bridges that gap by:
- Routing cost signals to engineers with context
- Preventing overcommitment to unstable workloads
- Ensuring inefficiencies are fixed before commitments are made

## Key Insight

Engineers don’t purchase Savings Plans—but they control the workload behavior that makes commitments safe.

## Run the pipeline

```bash
python3 src/ingest_cur.py
python3 src/process_cost_signals.py
python3 src/generate_jira_payload.py
