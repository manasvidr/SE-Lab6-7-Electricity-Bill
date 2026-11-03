# Lab 6 — Code and Branch Coverage

The application module is preserved unchanged. The two test modules separately exercise line/statement coverage and branch coverage.

## Setup

```bash
python -m pip install pytest coverage
```

Run these commands from this directory so the application module is importable.

## Code coverage

```bash
coverage erase
coverage run --source=electricity_bill -m pytest CodeCoverageTest_17_electricity_bill.py -v
coverage report -m
```

Save a terminal screenshot showing at least 90% coverage.

## Branch coverage

```bash
coverage erase
coverage run --branch --source=electricity_bill -m pytest BranchCoverageTest_17_electricity_bill.py -v
coverage report -m
```

Save a terminal screenshot showing at least 90% branch coverage.

The tests were locally verified: 26 code-coverage tests passed; 21 branch-coverage tests passed. Both runs reported 100% coverage. Capture fresh screenshots from your own environment for submission.
