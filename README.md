# Cumberland Business Supply — six-week analyst apprenticeship

You are the junior analyst for a fictional office-supply distributor serving Middle Tennessee. The CFO asks: “Are we growing profitably, and can I trust the numbers?” Sales argues that volume is improving; finance suspects discounts and product mix. You own a defensible answer, not just a dashboard.

All company names, customers, transactions and findings in this package are synthetic. This is a teaching dataset, not evidence about real Tennessee businesses. The extract cutoff is **2025-12-31**; never use today's date for inactivity or future-date tests.

## Start here

1. Read docs/BUSINESS_BRIEF.md and docs/DATA_DICTIONARY.md.
2. Create a private GitHub repository from this folder. Do not publish solutions before mentor review.
3. Use Python 3.10+ with its built-in sqlite3 module. Run `python python/load_raw.py` from the repository root. This requires no external packages and creates work/analytics.sqlite.
4. Run `python python/run_sql.py sql/00_profile.sql` to verify setup. The database contains raw_* tables with TEXT columns. Do not query clean tables until you build them.
5. Read docs/WEEKLY_HOMEWORK.md; start Week 1 and Q01–Q10.
6. Keep originals unchanged. Store your cleaned exports under data/clean, SQL under sql, outputs under work and explanations under docs.

For Week 6 install Pandas with `python -m pip install -r requirements.txt` if available in your environment. Standard-library CSV arithmetic is an acceptable fallback. Power BI Desktop requires a compatible Windows environment; if unavailable, submit the same model and dashboard using an available BI tool and discuss the substitution with your mentor. A cloud account is unnecessary for these six weeks.

SQLite syntax is the reference dialect. Use ISO date strings, `strftime`, `julianday`, CTEs and window functions. If using PostgreSQL or DuckDB, document date-function changes and independently reconcile outputs. Do not silently mix dialects.

## Deliverable contract

Each week: tagged commit `week-N`, completed issue, query outputs, validation evidence and a short client memo. Each query submission states input layer, grain, business definition and at least one independent check. Your analysis must account for exclusions and disclose data limitations.

AI is allowed. Attempt the task first, record the prompt and edits, explain every clause and validate the result. Be ready to solve one related query without AI during each review. Use docs/AI_MISTAKES.md and docs/AI_USAGE.md.

Start with four folders of evidence: source data, transformation logic, reconciled outputs and decision narrative. The portfolio should let another analyst reproduce your work.
