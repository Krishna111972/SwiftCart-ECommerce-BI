# SwiftCart E-Commerce BI Project

## Project Overview

SwiftCart E-Commerce BI Project is an end-to-end business intelligence project built to analyze e-commerce sales and operational performance.

The project uses Python for supporting data-generation and validation scripts, SQL for database-side work, and Power BI for data modeling, DAX measures, interactive analysis, and dashboard reporting.

## Project Objectives

The dashboard provides visibility into:

- Revenue and profitability
- Orders and quantity sold
- Category performance
- Revenue trends over time
- Top cities by revenue
- Top products by revenue
- Customer-level performance
- Rider performance and delivery fees
- Year-based analysis and filtering

## Technology Stack

- **Python** — data-generation and validation/support scripts
- **SQL** — database and data validation work
- **Power BI** — data modeling, DAX, visualization, drill-through and dashboarding
- **DAX** — business measures and time-intelligence calculations

## Project Structure

```text
SwiftCart_BI_Project/
├── 01_Raw_Data/
├── 02_SQL/
│   └── Python_Scripts/
│       ├── check_data_quality.py
│       ├── generate_master_data.py
│       ├── generate_transaction_data.py
│       ├── reconcile_orders.py
│       └── validate_orders.py
├── 03_PowerBI/
│   └── Ecommerce_BI_Analytics_Dashboard.pbix
├── 04_DAX/
├── 05_Documentation/
├── 06_Screenshots/
└── 07_Portfolio/
```

## Data Model

The Power BI model is organized around fact and dimension tables.

### Fact Tables

- `FactOrder`
- `FactOrderItem`

### Dimension Tables

- `DimDate`
- `DimCustomer`
- `DimProduct`
- `DimRider`
- `DimWarehouse`
- `DimCity`

This structure supports analysis across orders, products, customers, riders, locations, warehouses and dates.

## Power BI Dashboard

### Executive Overview

The Executive Overview provides a high-level view of business performance.

It includes KPIs such as:

- Net Revenue
- Profit Margin %
- Total Quantity
- Total Orders
- Total Profit
- Total Discount
- Average Order Value
- Total Revenue

It also includes:

- Revenue Contribution by Category
- Monthly Revenue Trend
- Top 10 Cities by Revenue
- Total Profit by Category
- Revenue Time Intelligence
- Top 10 Products by Revenue

### Customer Analysis

The Customer Analysis page focuses on customer performance and customer-level business analysis.

### Rider Analysis

The Rider Analysis page includes:

- Rider Performance
- Top 10 Riders by Orders
- Top 10 Riders by Delivery Fees
- Top 10 Riders by Revenue

The Rider Performance table uses a Top 10 filter based on order count.

### Customer Details

The Customer Details page provides customer-level information through drill-through functionality.

Displayed information includes:

- Customer Name
- City
- Age Group
- Gender
- Category Revenue
- Total Orders

### Customer Tooltip

A dedicated Customer Tooltip page is included for contextual customer metrics using Power BI tooltip functionality.

## DAX / Analytics

The Power BI model contains measures for business KPIs and time-based analysis, including measures related to:

- Revenue
- Net Revenue
- Profit
- Profit Margin
- Orders
- Quantity
- Discount
- Average Order Value
- Category Revenue
- Revenue LY
- Revenue MTD
- Revenue YTD
- Revenue YoY %
- Revenue Rank

## Data Quality and Validation

The project includes Python support scripts for data quality and transaction validation:

- `check_data_quality.py`
- `generate_master_data.py`
- `generate_transaction_data.py`
- `reconcile_orders.py`
- `validate_orders.py`

These scripts are organized separately from the Power BI report.

## Interactive Features

The Power BI solution includes:

- Year filtering
- Visual-level Top N filtering
- Cross-filtering between visuals
- Drill-through
- Tooltip page
- Interactive dashboard visuals

## Project Outcome

The completed project provides a centralized analytical dashboard for exploring e-commerce revenue, profitability, customers, products, cities and rider performance.

The solution combines structured data preparation, SQL/database work, dimensional modeling, DAX calculations and Power BI visualization into a single BI project.

## Main Project Files

Power BI report:

`03_PowerBI/Ecommerce_BI_Analytics_Dashboard.pbix`

Supporting Python scripts:

`02_SQL/Python_Scripts/`

Documentation:

`05_Documentation/`
