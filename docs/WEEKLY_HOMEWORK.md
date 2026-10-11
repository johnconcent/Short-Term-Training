# Weekly homework and mentor handoff

Target 8–12 learner hours/week plus a 60–75-minute mentor session. If a gate fails, revise before moving on; calendar targets do not override correctness. Advanced work is optional. Week 1 data/code setup can use SQLite only; Pandas is introduced in Week 6. Commit small changes throughout each week.

## Week 1 — Discover and profile

**Mentor gives:** Read brief, validate environment, demonstrate raw grain and file loading; answer clarification questions without revealing defect IDs.

**Time plan:** 2h setup/Git; 3h profiling/Q01–Q10; 2h dictionary and quality report; 1h client memo; 1–2h revision.

**Assignments:** Q01–Q10; Python CSV row count and date validator using datetime; no dashboard yet.

**Required submission:** docs/data_quality_report.md, work/quality_issues.csv, docs/clarification_log.md, docs/row_reconciliation.csv, ten diagnostic SQL scripts.

**Acceptance gate:** Raw row counts match extracts; keys/blanks/date/numeric/normalization/orphan issues reviewed; promotional zeros correctly retained; no fabricated fixes.

**Review questions:** Explain one defect and one legitimate edge case. Why can a valid date still be unusable?

**Client memo:** 150–250 words: what changed, what you know, what you cannot conclude, one recommendation and one question for the sponsor. Tag the reviewed commit `week-1`.


## Week 2 — SQL fundamentals and conservative cleaning

**Mentor gives:** Approve documented cleaning rules; require a quarantine ledger and ask who must resolve exclusions.

**Time plan:** 2h SELECT/grouping practice; 3h Q11–Q20; 3h cleaning and reconciliation; 1h memo; 1h revision.

**Assignments:** Q11–Q20; implement clean_* tables or clean tables; optional standard-library Python normalization; SQL aggregates remain primary.

**Required submission:** sql/cleaning.sql or python/clean.py, data/clean/*.csv, work/quarantine.csv, sql/Q11.sql–Q20.sql, quality/revenue reconciliation.

**Acceptance gate:** Unique parent keys; usable FK relationships; counts reconcile; rerunning yields same outputs; money formula correct; exclusion impact disclosed.

**Review questions:** Explain WHERE vs HAVING. What is lost when you quarantine a customer?

**Client memo:** 150–250 words: what changed, what you know, what you cannot conclude, one recommendation and one question for the sponsor. Tag the reviewed commit `week-2`.


## Week 3 — Joins, CTEs and business interpretation

**Mentor gives:** Introduce CFO definitions for AOV, active customers and customer region. Give a deliberately flawed join for diagnosis.

**Time plan:** 2h joins/CTEs; 4h Q21–Q30; 2h validations; 1h recommendation; 1h revision.

**Assignments:** Q21–Q30; create sales view at completed retained line grain; use Python to assert join cardinality as an optional extension.

**Required submission:** sql/create_sales_view.sql, sql/Q21.sql–Q30.sql, docs/metric_definitions.md, docs/findings_week3.md.

**Acceptance gate:** No join fan-out; AOV distinct orders; no-sale customers retained; inactivity fixed cutoff; each measure has an independent check.

**Review questions:** Why does AVG(line revenue) fail as AOV? Explain LEFT JOIN filtering.

**Client memo:** 150–250 words: what changed, what you know, what you cannot conclude, one recommendation and one question for the sponsor. Tag the reviewed commit `week-3`.


## Week 4 — Window functions and dimensional design

**Mentor gives:** Require a model before visuals; challenge sparse months and tied rankings; introduce star schema and basic SCD concept only.

**Time plan:** 2h window tutorials applied to client; 4h Q31–Q40; 2h model/calendar; 1h review; 1h revision.

**Assignments:** Q31–Q40; build monthly calendar scaffold and date dimension; document model relationships and fact grain.

**Required submission:** sql/Q31.sql–Q40.sql, docs/model.md with Mermaid diagram, docs/architecture.md, docs/validation_week4.md.

**Acceptance gate:** Stable tie-breaks; first-period growth blank; zero months included where needed; four months used for three declines; unique dimension keys.

**Review questions:** How would missing months change LAG and rolling totals? Why can RANK return more than three rows?

**Client memo:** 150–250 words: what changed, what you know, what you cannot conclude, one recommendation and one question for the sponsor. Tag the reviewed commit `week-4`.


## Week 5 — Power BI and financial reconciliation

**Mentor gives:** Act as CFO: demand a report that identifies an action. Provide the BI acceptance checklist; approve metric definitions first.

**Time plan:** 2h model/DAX practice; 3h Q41–Q50 and CSV export; 3h dashboard; 1h reconciliation; 1h revision.

**Assignments:** Q41–Q50; create exports and three-page BI report; DAX ratios, distinct counts, prior-month measures.

**Required submission:** dashboard/Cumberland.pbix if Power BI available, screenshots of three pages, dashboard/reconciliation.csv, docs/bi_design.md.

**Acceptance gate:** Relationships many-to-one, single direction; date marked; financial totals match SQL; cancellation denominator separate; cards respond consistently to filters.

**Review questions:** Why is gross margin a ratio of sums? Show what happens when you filter a category.

**Client memo:** 150–250 words: what changed, what you know, what you cannot conclude, one recommendation and one question for the sponsor. Tag the reviewed commit `week-5`.


## Week 6 — Python verification and client handoff

**Mentor gives:** Provide an incorrect AI margin query; conduct a presentation and independent coding check. Let him own final recommendations.

**Time plan:** 2h Pandas basics; 3h Q51–Q60; 2h reproducibility and Git cleanup; 1h executive memo; 1–2h rehearsal/revision.

**Assignments:** Q51–Q60; replicate revenue/monthly analysis in Python; classify quality issues; reconcile Python↔SQL↔BI; finish AI mistake log.

**Required submission:** python/reconcile.py or notebook, work/python_reconciliation.csv, docs/executive_memo.md, docs/AI_MISTAKES.md, release week-6.

**Acceptance gate:** Fresh rerun works; per-month totals reconcile; three measurable actions; limits explicit; can explain AI edits and write one related query without AI.

**Review questions:** What should management do Monday? How could exclusions change your answer? What did AI do and how did you check it?

**Client memo:** 150–250 words: what changed, what you know, what you cannot conclude, one recommendation and one question for the sponsor. Tag the reviewed commit `week-6`.


## Repeatable 75-minute mentoring session

10 minutes progress/blockers; 20 minutes live demo; 20 minutes query/model review; 15 minutes client challenge; 10 minutes next-week scope. Ask for evidence before offering solutions. Record no more than three priority fixes. Each session includes a five-minute related query explained or written without AI.

## Git practices from Week 1

Create a branch per change, make focused commits, open a local review/PR with the template, fix feedback, merge and tag the reviewed week. Never commit credentials, real personal data, large generated databases, local virtual environments or the mentor answer key. Synthetic CSVs may be committed with the fictional-data disclosure. Publishing to GitHub or LinkedIn happens only after your own final review; this package does not publish anything.

## Catch-up policy

If setup consumes Week 1, defer optional Python work. If SQL joins remain weak in Week 3, use Week 4 for remediation and reduce advanced window tasks until the gate passes. A BI substitute can demonstrate concepts, but does not establish Power BI competence. Do not add ML, cloud certification or autonomous agents to this foundation phase.
