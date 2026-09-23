import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. SETTINGS
# --------------------------------------------------

RAW_DIR = Path(".") / "01_Raw_Data"

# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

orders = pd.read_csv(
    RAW_DIR / "orders.csv",
    parse_dates=["OrderDate"]
)

customers = pd.read_csv(
    RAW_DIR / "customers.csv"
)

warehouses = pd.read_csv(
    RAW_DIR / "warehouses.csv"
)

riders = pd.read_csv(
    RAW_DIR / "riders.csv"
)


# --------------------------------------------------
# 3. BASIC CHECKS
# --------------------------------------------------

print("\n" + "=" * 60)
print("FACT_ORDER DATA QUALITY")
print("=" * 60)

print(f"Rows: {len(orders):,}")

print(
    f"Duplicate OrderID: "
    f"{orders['OrderID'].duplicated().sum():,}"
)

print("\nMissing values:")

missing = orders.isnull().sum()
missing = missing[missing > 0]

if len(missing) == 0:
    print("None")
else:
    print(missing)


# --------------------------------------------------
# 4. DATE VALIDATION
# --------------------------------------------------

print("\n" + "=" * 60)
print("DATE VALIDATION")
print("=" * 60)

print(f"Minimum Order Date: {orders['OrderDate'].min()}")
print(f"Maximum Order Date: {orders['OrderDate'].max()}")

invalid_dates = (
    (orders["OrderDate"] < "2024-01-01") |
    (orders["OrderDate"] > "2026-09-09")
).sum()

print(f"Orders outside date range: {invalid_dates:,}")


# --------------------------------------------------
# 5. FOREIGN KEY VALIDATION
# --------------------------------------------------

print("\n" + "=" * 60)
print("FOREIGN KEY VALIDATION")
print("=" * 60)

valid_customers = set(
    customers["CustomerKey"]
)

valid_warehouses = set(
    warehouses["WarehouseKey"]
)

valid_riders = set(
    riders["RiderKey"]
)

invalid_customers = (
    ~orders["CustomerKey"]
    .isin(valid_customers)
).sum()

invalid_warehouses = (
    ~orders["WarehouseKey"]
    .isin(valid_warehouses)
).sum()

invalid_riders = (
    ~orders["RiderKey"]
    .isin(valid_riders)
).sum()

print(
    f"Invalid CustomerKey: "
    f"{invalid_customers:,}"
)

print(
    f"Invalid WarehouseKey: "
    f"{invalid_warehouses:,}"
)

print(
    f"Invalid RiderKey: "
    f"{invalid_riders:,}"
)


# --------------------------------------------------
# 6. FINANCIAL VALIDATION
# --------------------------------------------------

print("\n" + "=" * 60)
print("FINANCIAL VALIDATION")
print("=" * 60)

calculated_total = (
    orders["OrderAmount"]
    - orders["DiscountAmount"]
    + orders["DeliveryFee"]
    + orders["TaxAmount"]
)

financial_errors = (
    abs(calculated_total - orders["TotalAmount"]) > 0.01
).sum()

print(
    f"Incorrect TotalAmount calculations: "
    f"{financial_errors:,}"
)


# --------------------------------------------------
# 7. BUSINESS RULES
# --------------------------------------------------

print("\n" + "=" * 60)
print("BUSINESS RULE VALIDATION")
print("=" * 60)

negative_amounts = (
    orders["OrderAmount"] < 0
).sum()

negative_discounts = (
    orders["DiscountAmount"] < 0
).sum()

discount_greater_than_order = (
    orders["DiscountAmount"]
    > orders["OrderAmount"]
).sum()

print(
    f"Negative OrderAmount: "
    f"{negative_amounts:,}"
)

print(
    f"Negative DiscountAmount: "
    f"{negative_discounts:,}"
)

print(
    f"Discount greater than OrderAmount: "
    f"{discount_greater_than_order:,}"
)


# --------------------------------------------------
# 8. STATUS VALIDATION
# --------------------------------------------------

print("\n" + "=" * 60)
print("ORDER STATUS VALIDATION")
print("=" * 60)

valid_statuses = {
    "Delivered",
    "Cancelled",
    "Failed",
    "Returned"
}

invalid_statuses = (
    ~orders["OrderStatus"]
    .isin(valid_statuses)
).sum()

print(
    f"Invalid OrderStatus: "
    f"{invalid_statuses:,}"
)


# --------------------------------------------------
# 9. FINAL RESULT
# --------------------------------------------------

print("\n" + "=" * 60)
print("FACT_ORDER VALIDATION COMPLETED")
print("=" * 60)