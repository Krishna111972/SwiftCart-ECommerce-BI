import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path

# --------------------------------------------------
# 1. SETTINGS
# --------------------------------------------------

fake = Faker("en_IN")
np.random.seed(42)

BASE_DIR = Path(".")
RAW_DIR = BASE_DIR / "01_Raw_Data"

RAW_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 2. CITY MASTER
# --------------------------------------------------

cities = [
    ["C001", "Mumbai", "Maharashtra", "West"],
    ["C002", "Pune", "Maharashtra", "West"],
    ["C003", "Bengaluru", "Karnataka", "South"],
    ["C004", "Hyderabad", "Telangana", "South"],
    ["C005", "Delhi", "Delhi", "North"],
    ["C006", "Indore", "Madhya Pradesh", "Central"],
    ["C007", "Jaipur", "Rajasthan", "North"],
    ["C008", "Ahmedabad", "Gujarat", "West"]
]

cities_df = pd.DataFrame(
    cities,
    columns=["CityKey", "City", "State", "Region"]
)

cities_df.to_csv(RAW_DIR / "cities.csv", index=False)


# --------------------------------------------------
# 3. WAREHOUSE MASTER
# --------------------------------------------------

warehouse_data = []

for i in range(1, 41):

    city = cities_df.sample(1).iloc[0]

    warehouse_data.append([
        f"W{i:03d}",
        f"WH-{city['City']}-{i:02d}",
        city["CityKey"],
        city["City"],
        np.random.choice(["Small", "Medium", "Large"])
    ])

warehouses_df = pd.DataFrame(
    warehouse_data,
    columns=[
        "WarehouseKey",
        "WarehouseName",
        "CityKey",
        "City",
        "WarehouseSize"
    ]
)

warehouses_df.to_csv(
    RAW_DIR / "warehouses.csv",
    index=False
)


# --------------------------------------------------
# 4. PRODUCT MASTER
# --------------------------------------------------

categories = {
    "Grocery": ["Rice", "Flour", "Dal", "Oil", "Spices"],
    "Beverages": ["Juice", "Coffee", "Tea", "Soft Drink", "Water"],
    "Snacks": ["Chips", "Biscuits", "Namkeen", "Chocolate"],
    "Personal Care": ["Shampoo", "Soap", "Toothpaste", "Face Wash"],
    "Household": ["Detergent", "Cleaner", "Tissue", "Garbage Bags"]
}

product_data = []

for i in range(1, 5001):

    category = np.random.choice(list(categories.keys()))
    subcategory = np.random.choice(categories[category])

    price = round(np.random.uniform(20, 1500), 2)

    product_data.append([
        f"P{i:05d}",
        f"{subcategory} Product {i}",
        category,
        subcategory,
        price,
        round(price * np.random.uniform(0.55, 0.85), 2)
    ])

products_df = pd.DataFrame(
    product_data,
    columns=[
        "ProductKey",
        "ProductName",
        "Category",
        "Subcategory",
        "SellingPrice",
        "UnitCost"
    ]
)

products_df.to_csv(
    RAW_DIR / "products.csv",
    index=False
)


# --------------------------------------------------
# 5. CUSTOMER MASTER
# --------------------------------------------------

customer_data = []

for i in range(1, 100001):

    city = cities_df.sample(1).iloc[0]

    customer_data.append([
        f"CUST{i:06d}",
        fake.name(),
        fake.email(),
        city["CityKey"],
        city["City"],
        np.random.choice(
            ["Male", "Female", "Other"],
            p=[0.48, 0.48, 0.04]
        ),
        np.random.choice(
            ["18-25", "26-35", "36-45", "46-55", "56+"]
        ),
        fake.date_of_birth(
            minimum_age=18,
            maximum_age=65
        )
    ])

customers_df = pd.DataFrame(
    customer_data,
    columns=[
        "CustomerKey",
        "CustomerName",
        "Email",
        "CityKey",
        "City",
        "Gender",
        "AgeGroup",
        "DateOfBirth"
    ]
)

customers_df.to_csv(
    RAW_DIR / "customers.csv",
    index=False
)


# --------------------------------------------------
# 6. RIDER MASTER
# --------------------------------------------------

rider_data = []

for i in range(1, 2001):

    city = cities_df.sample(1).iloc[0]

    rider_data.append([
        f"R{i:04d}",
        fake.name(),
        city["CityKey"],
        city["City"],
        np.random.choice(
            ["Full Time", "Part Time"]
        ),
        np.random.choice(
            ["Bike", "Scooter", "Electric Bike"]
        )
    ])

riders_df = pd.DataFrame(
    rider_data,
    columns=[
        "RiderKey",
        "RiderName",
        "CityKey",
        "City",
        "EmploymentType",
        "VehicleType"
    ]
)

riders_df.to_csv(
    RAW_DIR / "riders.csv",
    index=False
)


# --------------------------------------------------
# 7. SUMMARY
# --------------------------------------------------

print("====================================")
print("SwiftCart Master Data Generated")
print("====================================")

print(f"Cities      : {len(cities_df):,}")
print(f"Warehouses  : {len(warehouses_df):,}")
print(f"Products    : {len(products_df):,}")
print(f"Customers   : {len(customers_df):,}")
print(f"Riders      : {len(riders_df):,}")

print("\nFiles saved to:")
print(RAW_DIR.resolve())