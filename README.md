# CS262 Labs 6–7 — Electricity Bill

**Student repository:** https://github.com/manasvidr/SE-Lab6-7-Electricity-Bill  
**Assigned source repository:** https://github.com/SETAPESU26/L6_L7_17_electricity_bill

## Repository structure

- `Lab-6/electricity_bill.py` — original electricity-bill application, unchanged.
- `Lab-6/CodeCoverageTest_17_electricity_bill.py` — tests for statement/line coverage.
- `Lab-6/BranchCoverageTest_17_electricity_bill.py` — tests for decision-branch coverage.
- `Lab-6/reports/` — destination for terminal output and screenshots.

## Lab 6 — Coverage analysis

Install dependencies:

```bash
python -m pip install pytest coverage
```

Run the code-coverage suite from `Lab-6`:

```bash
coverage erase
coverage run --source=electricity_bill -m pytest CodeCoverageTest_17_electricity_bill.py -v
coverage report -m
```

Run the branch-coverage suite:

```bash
coverage erase
coverage run --branch --source=electricity_bill -m pytest BranchCoverageTest_17_electricity_bill.py -v
coverage report -m
```

The test suites were run against the unchanged application: the code-coverage suite passed 26 tests with 100% statement coverage; the branch suite passed 21 tests with 100% statement and branch coverage (22/22 branches). Re-run locally and save your own terminal screenshots in `Lab-6/reports/`.

## Lab 7

The Lab 7 handout/instructions were not included in the materials available when this repository was prepared. No Lab 7 implementation or deliverables are claimed yet. Add the exact Lab 7 requirements and artifacts here once the handout is available.
