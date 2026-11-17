# Software Engineering Lab — Lab 7 Report
## Fuzz Testing for Input Validation Bugs

**Student name:** ______________________________  
**Course / section:** ______________________________  
**Repository:** [manasvidr/SE-Lab6-7-Electricity-Bill](https://github.com/manasvidr/SE-Lab6-7-Electricity-Bill)  
**Branch:** `main`  
**Environment:** macOS · Python 3.15.0 · pytest 9.2.0 · Hypothesis 6.170.15

## 1. Objective
Use property-based fuzz testing to expose input-validation defects in the electricity-bill application, correct the defects, and rerun the test suite.

## 2. Functions under test
- `units_consumed(reading)`: calculates current minus previous meter reading from `previous:current`.
- `daily_average(units_csv)`: calculates the average of comma-separated daily unit values.
- `tariff_rate(code)`: calculates a rate from a supported `CATEGORY-SLAB` tariff code.

## 3. Test approach
The suite contains three Hypothesis-based fuzz tests, property-based tests for valid meter readings and daily-unit lists, and parameterized tests for valid tariff codes, malformed inputs, and non-string inputs. Invalid inputs are expected to raise `ValueError`.

## 4. Bugs observed in the original implementation
- Passing `None` or an integer to functions that call `.split()` raised `AttributeError`.
- Malformed or decreasing meter readings were not consistently rejected; consumption could be negative.
- Empty or malformed daily CSV values caused conversion errors.
- Unknown tariff categories or slabs raised `KeyError`.
- A spaced code such as ` COM - B ` was not normalized before lookup.

## 5. Fixes implemented
The corrected implementation validates input types and formats before processing. Meter readings must contain exactly two non-negative integers and the current reading cannot be lower than the previous reading. Daily CSV input must contain one or more non-negative integers. Tariff codes must contain one supported category and slab; whitespace and case are normalized. Invalid input raises `ValueError`.

## 6. Execution results

| Stage | Terminal result |
|---|---|
| Original implementation | **17 failed, 27 passed** (44 collected) |
| Corrected implementation | **44 passed in 0.21 seconds** |

The accompanying PDF report contains the actual before-and-after terminal screenshots supplied for this report.

## 7. Repository and commit evidence
- [Repository](https://github.com/manasvidr/SE-Lab6-7-Electricity-Bill)
- [Lab-7 folder](https://github.com/manasvidr/SE-Lab6-7-Electricity-Bill/tree/main/Lab-7)

The terminal verification showed `main` up to date with `origin/main` and a clean working tree. Recent commits included the validation fixes, Hypothesis tests, workflow documentation, and before/after examples.

## 8. Conclusion
Fuzz testing exposed input-validation defects in the original electricity-bill functions. After adding type, format, range, and lookup validation, the full 44-test suite passed. The terminal captures document the original failures and successful retest.

## Appendix
- Appendix A: Original implementation test failures (17 failed, 27 passed).
- Appendix B: Corrected implementation test results (44 passed in 0.21 seconds).

**Screenshot evidence:** See `Lab7_Fuzz_Testing_Report.pdf` in the submission package.