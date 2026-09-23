# 🛒 SwiftCart E-Commerce BI Project

> 📊 **End-to-end Business Intelligence project** for analyzing e-commerce sales, profitability, customers, products, cities, and rider performance.

---

## 🚀 Project Overview

SwiftCart E-Commerce BI is an end-to-end analytics solution built using **Python, SQL, Power BI, and DAX**.

The project combines data preparation and validation, SQL/database work, dimensional modeling, business measures, and interactive Power BI dashboards into one complete BI workflow.

### 🎯 Business Objectives

The dashboard helps analyze:

- 💰 Revenue & profitability
- 🛍️ Orders & quantity sold
- 📦 Product & category performance
- 📈 Revenue trends over time
- 🏙️ City-level performance
- 👥 Customer performance
- 🛵 Rider performance & delivery fees
- 📅 Year-based analysis

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Data generation, quality checks & validation |
| 🗄️ **SQL** | Database-side work & validation |
| 📊 **Power BI** | Data modeling, visualization & dashboarding |
| 📐 **DAX** | KPIs, calculations & time intelligence |

---

## 📁 Project Structure

```text
SwiftCart_BI_Project/
│
├── 01_Raw_Data/                         # Local raw datasets
│
├── 02_SQL/
│   ├── Python_scripts/
│   │   ├── check_data_quality.py
│   │   ├── generate_master_data.py
│   │   ├── generate_transaction_data.py
│   │   ├── reconcile_orders.py
│   │   └── validate_orders.py
│   │
│   └── swiftcart_sql.sql
│
├── 03_PowerBI/
│   └── Ecommerce_BI_Analytics_Dashboard.pbix
│
├── 04_DAX/
│   └── DAX_Measures.md
│
├── 05_Documentation/
│   ├── README.md
│   ├── Data_Dictionary.xlsx
│   ├── Project_Report.docx
│   ├── SQL_Documentation.md
│   └── PowerBI_Documentation.md
│
├── 06_Screenshots/                      # Dashboard screenshots
│
└── 07_Portfolio/                        # Portfolio materials
```

> 🔒 Raw data is kept outside the public GitHub repository when it may contain potentially sensitive information.

---

## 🧩 Data Model

The Power BI model follows a **fact + dimension** structure.

### 📌 Fact Tables

- `FactOrder`
- `FactOrderItem`

### 📚 Dimension Tables

- `DimDate`
- `DimCustomer`
- `DimProduct`
- `DimRider`
- `DimWarehouse`
- `DimCity`

This structure supports analysis across **orders, products, customers, riders, locations, warehouses, and dates**.

---

# 📊 Power BI Dashboard

## 🏠 Executive Overview

The Executive Overview provides a high-level view of overall business performance.

### 💳 KPI Cards

- 💰 Net Revenue
- 📈 Profit Margin %
- 📦 Total Quantity
- 🧾 Total Orders
- 💵 Total Profit
- 🏷️ Total Discount
- 🛒 Average Order Value
- 💰 Total Revenue

### 📈 Key Visuals

- 🥧 Revenue Contribution by Category
- 📅 Monthly Revenue Trend
- 🏙️ Top 10 Cities by Revenue
- 📊 Total Profit by Category
- ⏱️ Revenue Time Intelligence
- 🏆 Top 10 Products by Revenue

---

## 👥 Customer Analysis

The Customer Analysis page focuses on:

- Customer performance
- Revenue contribution
- Order activity
- Customer-level business analysis

---

## 🛵 Rider Analysis

The Rider Analysis page covers:

- 🛵 Rider Performance
- 🏆 Top 10 Riders by Orders
- 💰 Top 10 Riders by Delivery Fees
- 📊 Top 10 Riders by Revenue

The Rider Performance analysis uses a **Top 10 filter based on order count**.

---

## 🔎 Customer Details

The Customer Details page provides detailed customer-level information through **Power BI drill-through**.

Displayed information includes:

- 👤 Customer Name
- 🏙️ City
- 🎂 Age Group
- ⚧️ Gender
- 📊 Category Revenue
- 🧾 Total Orders

---

## 💬 Customer Tooltip

A dedicated **Customer Tooltip** page provides contextual customer metrics when used through Power BI tooltip functionality.

---

# 📐 DAX & Analytics

The Power BI model contains measures for:

- 💰 Revenue
- 💵 Net Revenue
- 📈 Profit
- 📊 Profit Margin
- 🧾 Orders
- 📦 Quantity
- 🏷️ Discount
- 🛒 Average Order Value
- 🗂️ Category Revenue
- 📅 Revenue LY
- 📆 Revenue MTD
- 📆 Revenue YTD
- 📈 Revenue YoY %
- 🏆 Revenue Rank

---

# 🧪 Data Quality & Validation

Python support scripts are included for data generation and validation:

- `check_data_quality.py`
- `generate_master_data.py`
- `generate_transaction_data.py`
- `reconcile_orders.py`
- `validate_orders.py`

These scripts support the data-quality and transaction-validation workflow before analysis.

---

# 🎛️ Interactive Features

The Power BI solution includes:

- 📅 Year filtering
- 🔝 Top N filtering
- 🔄 Cross-filtering
- 🔎 Drill-through
- 💬 Tooltip pages
- 📊 Interactive dashboard visuals

---

# 🔄 BI Workflow

```text
🐍 Python
   ↓
🗄️ SQL
   ↓
📐 Fact + Dimension Model
   ↓
📊 Power BI
   ↓
📐 DAX Measures
   ↓
📈 Interactive Dashboard
```

---

# 🏁 Project Outcome

SwiftCart BI provides a centralized analytical solution for exploring:

**Revenue • Profitability • Orders • Products • Customers • Cities • Riders**

The project demonstrates an end-to-end BI workflow covering:

**Data Preparation → SQL → Data Modeling → DAX → Visualization → Business Analysis**

---

## 📂 Main Project Files

### 📊 Power BI Report

`03_PowerBI/Ecommerce_BI_Analytics_Dashboard.pbix`

### 🐍 Python Scripts

`02_SQL/Python_scripts/`

### 🗄️ SQL

`02_SQL/swiftcart_sql.sql`

### 📐 DAX

`04_DAX/DAX_Measures.md`

### 📚 Documentation

`05_Documentation/`

---

## ⭐ Project Highlights

- 🔹 End-to-end BI workflow
- 🔹 Dimensional data model
- 🔹 SQL + Python data preparation
- 🔹 DAX business measures
- 🔹 Time-intelligence analysis
- 🔹 Top 10 business analysis
- 🔹 Drill-through & tooltip functionality
- 🔹 Interactive Power BI reporting

---

### 👨‍💻 SwiftCart E-Commerce BI

**Built with Python • SQL • Power BI • DAX**
