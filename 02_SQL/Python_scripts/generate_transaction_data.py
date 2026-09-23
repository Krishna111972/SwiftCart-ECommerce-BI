import pandas as pd
import numpy as np
from pathlib import Path

# ==================================================
# 1. SETTINGS
# ==================================================

np.random.seed(42)

RAW_DIR = Path(".") / "01_Raw_Data"

NUMBER_OF_ORDERS = 100_000

START_DATE = "2024-01-01"
END_DATE = "2026-09-09"


# ==================================================
# 2. LOAD MASTER DATA
# ==================================================

customers = pd.read_csv(RAW_DIR / "customers.csv")
warehouses = pd.read_csv(RAW_DIR / "warehouses.csv")
riders = pd.read_csv(RAW_DIR / "riders.csv")
products = pd.read_csv(RAW_DIR / "products.csv")


# ==================================================
# 3. PREPARE CITY MAPPINGS
# ==================================================

warehouse_by_city = (
    warehouses
    .groupby("CityKey")["WarehouseKey"]
    .apply(list)
    .to_dict()
)

rider_by_city = (
    riders
    .groupby("CityKey")["RiderKey"]
    .apply(list)
    .to_dict()
)


# ==================================================
# PART A — BASIC ORDER INFORMATION
# ==================================================

# --------------------------------------------------
# 4. ORDER DATES
# --------------------------------------------------

dates = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="D"
)

day_weights = np.where(
    dates.dayofweek >= 5,
    1.35,
    1.0
)

day_weights = day_weights / day_weights.sum()

order_dates = np.random.choice(
    dates,
    size=NUMBER_OF_ORDERS,
    p=day_weights
)


# --------------------------------------------------
# 5. CUSTOMERS
# --------------------------------------------------

customer_indices = np.random.randint(
    0,
    len(customers),
    size=NUMBER_OF_ORDERS
)

selected_customers = customers.iloc[
    customer_indices
].reset_index(drop=True)


# --------------------------------------------------
# 6. WAREHOUSE + RIDER
# --------------------------------------------------

warehouse_keys = []
rider_keys = []

for city_key in selected_customers["CityKey"]:

    warehouse_keys.append(
        np.random.choice(
            warehouse_by_city[city_key]
        )
    )

    rider_keys.append(
        np.random.choice(
            rider_by_city[city_key]
        )
    )


# --------------------------------------------------
# 7. ORDER STATUS
# --------------------------------------------------

order_status = np.random.choice(
    [
        "Delivered",
        "Cancelled",
        "Failed",
        "Returned"
    ],
    size=NUMBER_OF_ORDERS,
    p=[0.90, 0.05, 0.02, 0.03]
)


# --------------------------------------------------
# 8. PAYMENT METHOD
# --------------------------------------------------

payment_method = np.random.choice(
    [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Cash",
        "Wallet",
        "Net Banking"
    ],
    size=NUMBER_OF_ORDERS,
    p=[0.40, 0.20, 0.15, 0.10, 0.10, 0.05]
)


# --------------------------------------------------
# 9. ORDER CHANNEL
# --------------------------------------------------

order_channel = np.random.choice(
    [
        "Mobile App",
        "Web",
        "Partner App"
    ],
    size=NUMBER_OF_ORDERS,
    p=[0.70, 0.20, 0.10]
)


# --------------------------------------------------
# 10. NUMBER OF PRODUCT LINES
# --------------------------------------------------

number_of_lines = np.random.choice(
    [1, 2, 3, 4, 5, 6],
    size=NUMBER_OF_ORDERS,
    p=[0.20, 0.25, 0.25, 0.15, 0.10, 0.05]
)


# ==================================================
# PART B — FACT_ORDER_ITEM
# ==================================================

print("\nGenerating order items...")


# --------------------------------------------------
# 11. REPEAT EACH ORDER BY NUMBER OF LINES
# --------------------------------------------------

order_repeated = orders_base = pd.DataFrame({
    "OrderID": [
        f"ORD{i:07d}"
        for i in range(1, NUMBER_OF_ORDERS + 1)
    ],
    "OrderDate": order_dates,
    "CustomerKey": selected_customers["CustomerKey"],
    "WarehouseKey": warehouse_keys,
    "RiderKey": rider_keys,
    "OrderStatus": order_status,
    "PaymentMethod": payment_method,
    "OrderChannel": order_channel,
    "NumberOfLines": number_of_lines
})

order_repeated = orders_base.loc[
    orders_base.index.repeat(
        orders_base["NumberOfLines"]
    )
].reset_index(drop=True)


# --------------------------------------------------
# 12. SELECT PRODUCTS
# --------------------------------------------------

order_item_count = len(order_repeated)

product_indices = np.random.randint(
    0,
    len(products),
    size=order_item_count
)

selected_products = products.iloc[
    product_indices
].reset_index(drop=True)


# --------------------------------------------------
# 13. QUANTITY
# --------------------------------------------------

quantity = np.random.choice(
    [1, 2, 3, 4],
    size=order_item_count,
    p=[0.55, 0.25, 0.15, 0.05]
)


# --------------------------------------------------
# 14. PRODUCT PRICES
# --------------------------------------------------

unit_price = selected_products[
    "SellingPrice"
].to_numpy()

unit_cost = selected_products[
    "UnitCost"
].to_numpy()


# --------------------------------------------------
# 15. GROSS AMOUNT
# --------------------------------------------------

gross_amount = np.round(
    unit_price * quantity,
    2
)


# --------------------------------------------------
# 16. ORDER-LEVEL GROSS TOTAL
# --------------------------------------------------

order_gross_totals = (
    pd.Series(gross_amount)
    .groupby(order_repeated["OrderID"])
    .transform("sum")
    .to_numpy()
)


# --------------------------------------------------
# 17. ORDER DISCOUNT RATE
# --------------------------------------------------

discount_rate = np.random.choice(
    [0, 0.05, 0.10, 0.15, 0.20],
    size=NUMBER_OF_ORDERS,
    p=[0.40, 0.20, 0.20, 0.15, 0.05]
)

orders_base["DiscountRate"] = discount_rate


# Map discount rate to repeated order rows
item_discount_rate = (
    order_repeated["OrderID"]
    .map(
        orders_base.set_index("OrderID")["DiscountRate"]
    )
    .to_numpy()
)


# --------------------------------------------------
# 18. ITEM DISCOUNT
# --------------------------------------------------

item_discount = np.round(
    gross_amount * item_discount_rate,
    2
)


# --------------------------------------------------
# 19. NET AMOUNT
# --------------------------------------------------

net_amount = np.round(
    gross_amount - item_discount,
    2
)


# --------------------------------------------------
# 20. COST
# --------------------------------------------------

cost_amount = np.round(
    unit_cost * quantity,
    2
)


# --------------------------------------------------
# 21. PROFIT
# --------------------------------------------------

profit_amount = np.round(
    net_amount - cost_amount,
    2
)


# --------------------------------------------------
# 22. CREATE FACT_ORDER_ITEM
# --------------------------------------------------

order_items = pd.DataFrame({

    "OrderItemID": [
        f"OI{i:08d}"
        for i in range(1, order_item_count + 1)
    ],

    "OrderID":
        order_repeated["OrderID"].to_numpy(),

    "ProductKey":
        selected_products["ProductKey"].to_numpy(),

    "Quantity":
        quantity,

    "UnitPrice":
        unit_price,

    "UnitCost":
        unit_cost,

    "GrossAmount":
        gross_amount,

    "DiscountAmount":
        item_discount,

    "NetAmount":
        net_amount,

    "CostAmount":
        cost_amount,

    "ProfitAmount":
        profit_amount
})


# ==================================================
# PART C — DERIVE ORDER FINANCIALS
# ==================================================

# --------------------------------------------------
# 23. AGGREGATE ITEMS TO ORDER LEVEL
# --------------------------------------------------

order_financials = (
    order_items
    .groupby("OrderID")
    .agg(
        OrderAmount=("GrossAmount", "sum"),
        DiscountAmount=("DiscountAmount", "sum")
    )
    .reset_index()
)


# --------------------------------------------------
# 24. DELIVERY FEE
# --------------------------------------------------

order_financials["DeliveryFee"] = np.where(
    order_financials["OrderAmount"] >= 500,
    0,
    np.random.choice(
        [20, 25, 30, 40],
        size=len(order_financials)
    )
)


# --------------------------------------------------
# 25. TAX
# --------------------------------------------------

order_financials["TaxAmount"] = np.round(
    (
        order_financials["OrderAmount"]
        - order_financials["DiscountAmount"]
    ) * 0.05,
    2
)


# --------------------------------------------------
# 26. TOTAL AMOUNT
# --------------------------------------------------

order_financials["TotalAmount"] = np.round(
    order_financials["OrderAmount"]
    - order_financials["DiscountAmount"]
    + order_financials["DeliveryFee"]
    + order_financials["TaxAmount"],
    2
)


# ==================================================
# PART D — CREATE FACT_ORDER
# ==================================================

orders = orders_base.merge(
    order_financials,
    on="OrderID",
    how="left"
)


# --------------------------------------------------
# 27. REMOVE HELPER COLUMN
# --------------------------------------------------

orders = orders.drop(
    columns=["DiscountRate"]
)


# --------------------------------------------------
# 28. SAVE FILES
# --------------------------------------------------

orders.to_csv(
    RAW_DIR / "orders.csv",
    index=False
)

order_items.to_csv(
    RAW_DIR / "order_items.csv",
    index=False
)


# ==================================================
# PART E — SUMMARY
# ==================================================

print("\n" + "=" * 60)
print("TRANSACTION DATA GENERATED")
print("=" * 60)

print(
    f"Orders      : {len(orders):,}"
)

print(
    f"Order Items : {len(order_items):,}"
)

print(
    f"Total Gross : "
    f"₹{order_items['GrossAmount'].sum():,.2f}"
)

print(
    f"Total Discount : "
    f"₹{order_items['DiscountAmount'].sum():,.2f}"
)

print(
    f"Total Profit : "
    f"₹{order_items['ProfitAmount'].sum():,.2f}"
)

print("\nFiles saved:")

print(
    (RAW_DIR / "orders.csv").resolve()
)

print(
    (RAW_DIR / "order_items.csv").resolve()
)