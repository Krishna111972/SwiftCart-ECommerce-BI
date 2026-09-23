import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. SETTINGS
# --------------------------------------------------

RAW_DIR = Path(".") / "01_Raw_Data"


# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

cities = pd.read_csv(RAW_DIR / "cities.csv")
warehouses = pd.read_csv(RAW_DIR / "warehouses.csv")
products = pd.read_csv(RAW_DIR / "products.csv")
customers = pd.read_csv(RAW_DIR / "customers.csv")
riders = pd.read_csv(RAW_DIR / "riders.csv")


# --------------------------------------------------
# 3. HELPER FUNCTION
# --------------------------------------------------

def check_table(df, table_name, primary_key):

    print("\n" + "=" * 60)
    print(f"DATA QUALITY REPORT: {table_name}")
    print("=" * 60)

    # Row count
    print(f"Rows: {len(df):,}")

    # Duplicate primary keys
    duplicate_count = df[primary_key].duplicated().sum()
    print(f"Duplicate {primary_key}: {duplicate_count:,}")

    # Missing values
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("Missing values: None")
    else:
        print("Missing values:")
        print(missing)

    return duplicate_count


# --------------------------------------------------
# 4. PRIMARY KEY CHECKS
# --------------------------------------------------

check_table(cities, "Cities", "CityKey")

check_table(
    warehouses,
    "Warehouses",
    "WarehouseKey"
)

check_table(
    products,
    "Products",
    "ProductKey"
)

check_table(
    customers,
    "Customers",
    "CustomerKey"
)

check_table(
    riders,
    "Riders",
    "RiderKey"
)


# --------------------------------------------------
# 5. PRODUCT VALIDATION
# --------------------------------------------------

print("\n" + "=" * 60)
print("PRODUCT BUSINESS RULE CHECKS")
print("=" * 60)

invalid_price = (
    products["SellingPrice"] <= 0
).sum()

invalid_cost = (
    products["UnitCost"] <= 0
).sum()

cost_higher_than_price = (
    products["UnitCost"] > products["SellingPrice"]
).sum()

print(f"Invalid selling prices: {invalid_price:,}")
print(f"Invalid unit costs: {invalid_cost:,}")
print(f"Cost higher than selling price: {cost_higher_than_price:,}")


# --------------------------------------------------
# 6. CUSTOMER VALIDATION
# --------------------------------------------------

print("\n" + "=" * 60)
print("CUSTOMER BUSINESS RULE CHECKS")
print("=" * 60)

duplicate_emails = customers["Email"].duplicated().sum()

valid_age_groups = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56+"
]

invalid_age_groups = (
    ~customers["AgeGroup"].isin(valid_age_groups)
).sum()

print(f"Duplicate emails: {duplicate_emails:,}")
print(f"Invalid age groups: {invalid_age_groups:,}")


# --------------------------------------------------
# 7. FOREIGN KEY CHECKS
# --------------------------------------------------

print("\n" + "=" * 60)
print("FOREIGN KEY CHECKS")
print("=" * 60)

valid_city_keys = set(cities["CityKey"])

invalid_warehouse_cities = (
    ~warehouses["CityKey"].isin(valid_city_keys)
).sum()

invalid_customer_cities = (
    ~customers["CityKey"].isin(valid_city_keys)
).sum()

invalid_rider_cities = (
    ~riders["CityKey"].isin(valid_city_keys)
).sum()

print(
    f"Warehouses with invalid CityKey: "
    f"{invalid_warehouse_cities:,}"
)

print(
    f"Customers with invalid CityKey: "
    f"{invalid_customer_cities:,}"
)

print(
    f"Riders with invalid CityKey: "
    f"{invalid_rider_cities:,}"
)


# --------------------------------------------------
# 8. FINAL RESULT
# --------------------------------------------------

print("\n" + "=" * 60)
print("DATA QUALITY CHECK COMPLETED")
print("=" * 60)

print("Master data validation finished.")

# --------------------------------------------------
# 9. INVESTIGATE DUPLICATE EMAILS
# --------------------------------------------------

print("\n" + "=" * 60)
print("DUPLICATE EMAIL INVESTIGATION")
print("=" * 60)

duplicate_email_rows = customers[
    customers["Email"].duplicated(keep=False)
].sort_values("Email")

print(
    f"Customers involved in duplicate emails: "
    f"{len(duplicate_email_rows):,}"
)

print("\nSample duplicate records:")

print(
    duplicate_email_rows[
        [
            "CustomerKey",
            "CustomerName",
            "Email",
            "City",
            "Gender",
            "AgeGroup"
        ]
    ].head(20).to_string(index=False)
)