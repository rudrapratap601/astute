# ASTUTE — Project Tracker

> Working plan based on **ASTUTE Intelligent Decision & Analytics Platform.pdf**. The document also uses NEXUS; this tracker uses ASTUTE. All tasks below are proposed and start in Backlog; no implementation progress, dates, or owners have been assumed.

## Project purpose

Turn uploaded data into trustworthy analysis, actionable insights, and eventually predictions. Build a real data-processing and analytics pipeline, with an AI analyst added after the analytics foundation.

## Dashboard

- **Current focus:** V0 — Analytics Engine (proposed starting point)
- **This week's outcome:** Fill in during weekly planning.
- **Next action:** Confirm V0 acceptance criteria and choose a representative test CSV.
- **Progress:** Completed tasks / total tasks within the active version. Exclude Cancelled tasks.
- **Main blocker:** Link the most important open challenge.
- **Latest learning:** Link a development journal entry.

Recommended Notion dashboard views: This Week; Task Board by Status; V0 Backlog; Blocked Tasks; Open Challenges; Latest Plans; Resolved Challenges.

## Roadmap

The scope column follows the PDF. Exit criteria are suggested implementation checkpoints.

| Version | Milestone | Scope | Suggested exit criterion | Status |
| --- | --- | --- | --- | --- |
| V0 | Analytics Engine | CSV upload, validation, profiling, problem detection, cleaning plan, user approval, cleaning, analysis, insights, results/report | A representative CSV completes the full flow; cleaning requires approval; a report explains findings and data-quality limitations | Backlog |
| V1 | Data Platform | Multiple sources, ETL, PostgreSQL, analytics engine, dashboard | Data from selected sources can be loaded repeatably into PostgreSQL and explored in a dashboard | Backlog |
| V2 | ML Intelligence | Feature engineering, training pipeline, model registry, predictions and explainability | A versioned model produces evaluated predictions with appropriate explanations | Backlog |
| V3 | AI Analyst | User question, agent routing to SQL/statistics/ML, evidence, answer and visualization | Questions produce evidence-backed answers and charts using the analytical tools | Backlog |
| V4 | Production Engineering | Async jobs, queues/caching where needed, Docker, CI/CD, monitoring, authentication | Deployment is repeatable; jobs and failures are observable; access is controlled | Backlog |
| V5 | Advanced Intelligence | Multi-dataset reasoning, RAG over reports/metadata, anomaly detection, forecasting, automated workflows, model monitoring, specialized agents | Selected advanced capabilities demonstrate value on agreed evaluation datasets | Backlog |

Note: The version order reflects the PDF. Essential access controls and data handling should be included whenever real users or sensitive data are introduced, even before V4.

## Tasks database

Create one Notion database with these properties:

| Property | Type | Values / purpose |
| --- | --- | --- |
| Task | Title | Concrete deliverable |
| ID | Text | Stable reference, such as V0-01 |
| Version | Select | V0, V1, V2, V3, V4, V5 |
| Component | Select | Product, Ingestion, Validation, Profiling, Cleaning, Analytics, Insights, Reporting, Infrastructure, ML, AI |
| Status | Status | Backlog, Ready, In Progress, Blocked, In Review, Done; optional Cancelled |
| Priority | Select | P0, P1, P2 |
| Owner | Person | Assign when known |
| Start / Due | Date | Set after estimating |
| Sprint / Week | Text | Planning period |
| Estimate | Number | Hours or points; pick one consistently |
| Depends on | Relation → Tasks | Prerequisites |
| Plans | Relation → Plans & Journal | Implementation plans and work logs |
| Challenges | Relation → Challenges & Solutions | Problems affecting this task |
| Evidence | URL | PR, commit, demo, or test evidence |

### Initial V0 backlog

Priorities and dependencies are suggestions, not requirements from the PDF. Every row starts in Backlog.

| ID | Task | Component | Priority | Depends on | Acceptance criteria |
| --- | --- | --- | --- | --- | --- |
| V0-01 | Define V0 scope and acceptance dataset | Product | P0 | — | Document supported CSV inputs, expected outputs, constraints, and one representative end-to-end example |
| V0-02 | Implement CSV upload and parsing | Ingestion | P0 | V0-01 | Valid CSV loads; empty, malformed, and unsupported input produces useful errors |
| V0-03 | Implement dataset validation | Validation | P0 | V0-02 | Validation results distinguish blocking errors from warnings and identify affected fields |
| V0-04 | Build the data profiler | Profiling | P0 | V0-03 | Show dimensions, inferred types, missingness, uniqueness, and relevant descriptive statistics |
| V0-05 | Build the data problem detector | Profiling | P0 | V0-04 | Surface supported data-quality issues with evidence; distinguish suspicious values from confirmed errors |
| V0-06 | Generate a reviewable cleaning plan | Cleaning | P0 | V0-05 | Each proposed transformation includes its reason, target, expected effect, and limitations |
| V0-07 | Add cleaning approval and rejection | Cleaning | P0 | V0-06 | User can review and approve or reject the plan; execution cannot bypass approval |
| V0-08 | Implement approved cleaning operations | Cleaning | P0 | V0-07 | Only approved operations run; preserve original data and record changes and failures |
| V0-09 | Build the analysis engine | Analytics | P0 | V0-08 | Defined analysis operations return reproducible results and handle unsupported columns gracefully |
| V0-10 | Build the insight engine | Insights | P1 | V0-09 | Each insight links to computed evidence and states relevant limitations |
| V0-11 | Build results and report experience | Reporting | P1 | V0-10 | Present quality findings, cleaning history, analysis, and insights in an understandable report |
| V0-12 | Validate the complete V0 workflow | Product | P0 | V0-11 | Representative and problematic inputs exercise the full workflow, including rejected cleaning and failures |

### Task page template

**Outcome:** What will the user or system be able to do?

**Acceptance criteria**
- [ ] Observable result
- [ ] Relevant failure behavior
- [ ] Evidence captured

**Implementation plan:** Link a plan or outline the steps here.

**Dependencies:** Link prerequisite tasks.

**Challenges:** Link challenge records, rather than burying blockers in comments.

**Validation:** Input tested, expected result, actual result, and evidence.

**Completion note:** What changed, remaining limitations, and follow-up tasks.

## Plans & Journal database

| Property | Type | Purpose |
| --- | --- | --- |
| Entry | Title | Plan or journal entry name |
| Type | Select | Weekly Plan, Implementation Plan, Daily Log, Retrospective |
| Date / Period | Date | Day or date range |
| Status | Select | Draft, Active, Completed, Superseded |
| Version | Select | V0–V5 |
| Tasks | Relation → Tasks | Work covered |
| Challenges | Relation → Challenges & Solutions | Problems discussed |
| Outcome | Text | Brief result or learning |

### Implementation plan template

**Objective:**

**Related tasks:**

**Current state and assumptions:**

**Proposed approach:**

**Steps**
1. Define the expected behavior.
2. Implement the smallest useful slice.
3. Validate relevant success and failure cases.
4. Record evidence and follow-up work.

**Alternatives and tradeoffs:**

**Risks / unknowns:**

**Definition of done:**

**Actual outcome / changes to plan:**

### Weekly plan template

**Week:**

**One primary outcome:**

**Committed tasks:** Link a realistic set of tasks.

**Stretch work:**

**Dependencies / blockers:**

**End-of-week review:** Completed; carried over and why; lessons; next priority.

### Daily development log template

**Today's intention:**

**What I implemented:**

**What failed or surprised me:** Link challenges.

**How I investigated / solved it:**

**What I learned:**

**Next action:**

## Challenges & Solutions database

Keep each challenge and its solution in the same record so the investigation history stays searchable. Do not mark a challenge resolved until its fix has been verified.

| Property | Type | Purpose |
| --- | --- | --- |
| Challenge | Title | Specific symptom or question |
| ID | Text | CH-001, CH-002, etc. |
| Status | Select | Open, Investigating, Fix in Progress, Validating, Resolved, Deferred |
| Severity | Select | Blocker, High, Medium, Low |
| Category | Select | Bug, Data Quality, Design, Performance, Dependency, Learning |
| Discovered | Date | First observed |
| Resolved | Date | Set only after verification |
| Version | Select | V0–V5 |
| Related tasks | Relation → Tasks | Affected deliverables |
| Related plans | Relation → Plans & Journal | Investigation or work log |
| Root cause | Text | Short confirmed explanation |
| Solution summary | Text | Searchable account of the fix |
| Evidence | URL | Test result, commit, PR, or supporting notes |

### Challenge page template

**Problem and impact:** What happened, and what does it prevent?

**Expected vs. actual behavior:**

**Reproduction steps / sample input:**

**Environment / relevant versions:**

**Evidence:** Error messages, relevant logs, screenshots, or minimal examples. Remove secrets and sensitive data.

**Hypotheses:** Keep assumptions separate from confirmed causes.

**Investigation log**

| Attempt / date | Hypothesis | Action taken | Result | Next step |
| --- | --- | --- | --- | --- |
| | | | | |

**Confirmed root cause:**

**Solution implemented:** Explain what changed and why it addresses the cause.

**Verification:** Describe the original reproduction after the fix and relevant regression checks.

**Prevention / lesson learned:**

**Remaining work:** Link follow-up tasks.

### Example only — not an observed project issue

**Challenge:** CSV identifier column loses leading zeros.

**Related task:** V0-02.

**Expected vs. actual:** Identifier `00123` should remain unchanged but appears as `123`.

**Hypothesis:** Automatic type inference treated the identifier as numeric.

**Investigation:** Compare source text, parser settings, and parsed values; test mixed and zero-prefixed identifiers.

**Possible solution:** Support explicit column types and preserve identifiers as text.

**Verification required:** Confirm `00123` survives upload and reporting, while genuine numerical columns still work correctly.

This is a usage example only; do not count it as a real blocker or a completed fix.

## Working routine

1. Start the week with a Weekly Plan and select a small set of Ready tasks.
2. Move a task to In Progress when you start; record the approach in an Implementation Plan.
3. When a problem needs investigation, create a challenge, link the task, and record attempts. Mark the task Blocked only if progress cannot continue.
4. Record the root cause, solution, and validation before resolving the challenge.
5. Attach completion evidence before marking the task Done.
6. Review the active version weekly, update the next action, and capture lessons in the journal.

## Notion setup status

This file is the prepared tracker content and database specification. It is not yet a live Notion workspace. Creating databases, relations, views, and reusable templates requires the Notion connection and a destination page. Current implementation progress and scheduling remain unconfirmed.
