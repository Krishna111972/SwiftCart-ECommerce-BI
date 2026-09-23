import pandas as pd
from pathlib import Path

RAW_DIR = Path(".") / "01_Raw_Data"

orders = pd.read_csv(RAW_DIR / "orders.csv")
order_items = pd.read_csv(RAW_DIR / "order_items.csv")

# --------------------------------------------------
# 1. AGGREGATE ORDER ITEMS
# --------------------------------------------------

item_summary = (
    order_items
    .groupby("OrderID")
    .agg(
        ItemGrossAmount=("GrossAmount", "sum"),
        ItemDiscountAmount=("DiscountAmount", "sum"),
        ItemNetAmount=("NetAmount", "sum"),
        ItemCostAmount=("CostAmount", "sum"),
        ItemProfitAmount=("ProfitAmount", "sum")
    )
    .reset_index()
)

# --------------------------------------------------
# 2. JOIN WITH ORDERS
# --------------------------------------------------

comparison = orders.merge(
    item_summary,
    on="OrderID",
    how="left"
)

# --------------------------------------------------
# 3. CHECK RECONCILIATION
# --------------------------------------------------

comparison["GrossDifference"] = (
    comparison["ItemGrossAmount"]
    - comparison["OrderAmount"]
)

comparison["DiscountDifference"] = (
    comparison["ItemDiscountAmount"]
    - comparison["DiscountAmount"]
)

print("\n" + "=" * 60)
print("ORDER ↔ ORDER ITEM RECONCILIATION")
print("=" * 60)

print(
    f"Orders: {len(comparison):,}"
)

print(
    f"Orders with item data: "
    f"{comparison['ItemGrossAmount'].notna().sum():,}"
)

print("\nTotal values:")

print(
    f"Order-level amount : "
    f"₹{comparison['OrderAmount'].sum():,.2f}"
)

print(
    f"Item-level gross   : "
    f"₹{comparison['ItemGrossAmount'].sum():,.2f}"
)

print(
    f"Order-level discount: "
    f"₹{comparison['DiscountAmount'].sum():,.2f}"
)

print(
    f"Item-level discount : "
    f"₹{comparison['ItemDiscountAmount'].sum():,.2f}"
)

# --------------------------------------------------
# 4. DIFFERENCE
# --------------------------------------------------

gross_difference = (
    comparison["GrossDifference"].abs() > 0.01
).sum()

discount_difference = (
    comparison["DiscountDifference"].abs() > 0.01
).sum()

print("\nReconciliation failures:")

print(
    f"Gross amount mismatches: "
    f"{gross_difference:,}"
)

print(
    f"Discount mismatches: "
    f"{discount_difference:,}"
)

# --------------------------------------------------
# 5. SAMPLE
# --------------------------------------------------

print("\nSample comparison:")

print(
    comparison[
        [
            "OrderID",
            "OrderAmount",
            "ItemGrossAmount",
            "DiscountAmount",
            "ItemDiscountAmount",
            "GrossDifference"
        ]
    ]
    .head(10)
    .to_string(index=False)
)