"""Validated electricity-bill helper functions for Lab 7 fuzz testing."""
RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}

def units_consumed(reading):
    """Return current minus previous meter reading."""
    if not isinstance(reading, str):
        raise ValueError("reading must be a string in previous:current format")
    parts = reading.split(":")
    if len(parts) != 2 or not all(part.strip().isdigit() for part in parts):
        raise ValueError("reading must contain exactly two non-negative integers")
    previous, current = (int(part.strip()) for part in parts)
    if current < previous:
        raise ValueError("current reading cannot be less than previous reading")
    return current - previous

def daily_average(units_csv):
    """Return the mean of a non-empty CSV of non-negative integers."""
    if not isinstance(units_csv, str):
        raise ValueError("daily units must be supplied as a CSV string")
    parts = units_csv.split(",")
    if not parts or any(not part.strip().isdigit() for part in parts):
        raise ValueError("CSV must contain one or more non-negative integers")
    units = [int(part.strip()) for part in parts]
    return round(sum(units) / len(units), 2)

def tariff_rate(code):
    """Return the rate for a supported CATEGORY-SLAB code."""
    if not isinstance(code, str):
        raise ValueError("tariff code must be a string")
    parts = code.split("-")
    if len(parts) != 2:
        raise ValueError("tariff code must have CATEGORY-SLAB format")
    category, slab = (part.strip().upper() for part in parts)
    if category not in RATES:
        raise ValueError("unknown tariff category")
    if slab not in SLAB:
        raise ValueError("unknown tariff slab")
    return RATES[category] * SLAB[slab]

def main():
    print("==== Running units_consumed ====")
    print("Units Consumed:", units_consumed(input("Enter meter readings as previous:current (e.g. 1200:1350): ")))
    print("\n==== Running daily_average ====")
    print("Daily Average:", daily_average(input("Enter daily units as CSV (e.g. 5,7,6): ")))
    print("\n==== Running tariff_rate ====")
    print("Rate per Unit:", tariff_rate(input("Enter a tariff code (e.g. DOM-A): ")))

if __name__ == "__main__":
    main()
