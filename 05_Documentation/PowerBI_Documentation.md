# SwiftCart BI — Power BI Documentation

## 1. Report Overview

The SwiftCart Power BI report provides interactive analysis of e-commerce sales and operational performance.

The report combines a dimensional data model, DAX measures, filters, Top N analysis, drill-through, and tooltip functionality.

## 2. Data Model

The report uses the following analytical tables:

### Fact Tables
- `FactOrder`
- `FactOrderItem`

### Dimension Tables
- `DimCustomer`
- `DimCity`
- `DimDate`
- `DimProduct`
- `DimRider`
- `DimWarehouse`

The dimensions provide descriptive context for filtering and grouping while the fact tables provide transactional values for analysis.

## 3. Executive Overview

The Executive Overview provides a consolidated business-performance view.

### KPI Areas

The page includes KPI measures covering:

- Net Revenue
- Total Revenue
- Total Profit
- Profit Margin %
- Total Orders
- Total Quantity
- Total Discount
- Average Order Value

### Main Analysis

The page includes analysis such as:

- Revenue Contribution by Category
- Monthly Revenue Trend
- Top 10 Cities by Revenue
- Total Profit by Category
- Revenue Time Intelligence
- Top 10 Products by Revenue

## 4. Customer Analysis

The Customer Analysis page focuses on customer performance.

It supports analysis of customer revenue, orders, customer segments, and customer-level performance using the available customer dimensions and measures.

## 5. Rider Analysis

The Rider Analysis page focuses on delivery/rider performance.

It includes:

- Rider Performance
- Top 10 Riders by Orders
- Top 10 Riders by Delivery Fees
- Top 10 Riders by Revenue

The Rider Performance analysis uses a Top 10 filter based on order count.

## 6. Customer Details

The Customer Details page provides detailed customer-level information through Power BI drill-through functionality.

Relevant fields include:

- Customer Name
- City
- Age Group
- Gender
- Category Revenue
- Total Orders

## 7. Customer Tooltip

A dedicated Customer Tooltip page is available for contextual customer information when used through Power BI tooltip functionality.

## 8. Time Intelligence

The report contains time-based measures including:

- Revenue LY
- Revenue MTD
- Revenue YTD
- Revenue YoY %
- Revenue Rolling 30D

The `DimDate` table provides the calendar fields used for date-based analysis.

## 9. Top N Analysis

Top 10 analysis is used for key business comparisons, including:

- Top 10 Cities by Revenue
- Top 10 Products by Revenue
- Top 10 Customers by Revenue
- Top 10 Riders by Orders
- Top 10 Riders by Delivery Fees
- Top 10 Riders by Revenue

## 10. Interactive Features

The report supports:

- Year filtering
- Cross-filtering between visuals
- Top N filtering
- Drill-through
- Tooltip pages
- Interactive visual analysis

## 11. Measure Organization

Measures are maintained in the `Measures_Table` table and organized using Power BI display folders:

- `Revenue`
- `Time Intelligence`
- `Performance`
- `Ranking`
- `Customer`

This keeps the model easier to navigate without changing the underlying DAX logic.

## 12. DAX Measure Groups

The report contains measures covering:

- Revenue
- Profitability
- Orders
- Quantity
- Discounts
- Average Order Value
- Customer analysis
- Ranking
- Time intelligence

The exact DAX expressions remain in the `.pbix` file and the separate `04_DAX/DAX_Measures.md` reference file.

## 13. Main Power BI File

The final Power BI report is stored at:

`03_PowerBI/Ecommerce_BI_Analytics_Dashboard.pbix`

## 14. Documentation Note

This document describes the confirmed structure and functionality of the Power BI report. The `.pbix` file remains the source of truth for exact visual configuration, relationships, formatting, and DAX expressions.
