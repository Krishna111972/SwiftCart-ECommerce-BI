# SwiftCart BI — SQL Documentation

## 1. Purpose

The SQL layer supports the SwiftCart e-commerce BI project by providing the database-side foundation used for analysis and Power BI reporting.

SQL work covers database/table setup, data validation, and preparation of structured fact and dimension data.

## 2. Analytical Model

The final Power BI model uses the following main tables:

### Fact Tables

- `FactOrder` — order-level transactional data.
- `FactOrderItem` — product/order-line transactional data.

### Dimension Tables

- `DimCustomer` — customer attributes.
- `DimCity` — city and geographic attributes.
- `DimDate` — calendar and time attributes.
- `DimProduct` — product and category attributes.
- `DimRider` — rider attributes.
- `DimWarehouse` — warehouse attributes.

## 3. Database Work

The SQL stage supports:

- Database and table setup
- Loading/working with structured e-commerce data
- Primary/business key handling
- Foreign-key relationships between analytical entities
- Data validation and reconciliation
- Preparation of data for BI analysis

## 4. Data Validation

Validation activities were used to check the consistency of the underlying data before/while building the BI solution.

The project also contains supporting Python scripts for data-quality and transaction validation:

- `check_data_quality.py`
- `generate_master_data.py`
- `generate_transaction_data.py`
- `reconcile_orders.py`
- `validate_orders.py`

## 5. Fact and Dimension Relationships

The model follows a dimensional approach:

```text
DimCustomer ──┐
DimProduct  ──┤
DimDate     ──┤
DimRider    ──┼──> FactOrder / FactOrderItem
DimWarehouse──┤
DimCity     ──┘
```

The dimensions provide descriptive/filtering context while the fact tables provide transactional values used for aggregation and KPI calculations.

## 6. SQL to Power BI Flow

```text
Source / Prepared Data
        ↓
SQL Database
        ↓
Fact + Dimension Tables
        ↓
Power BI Data Model
        ↓
DAX Measures
        ↓
Interactive Dashboard
```

## 7. Project SQL Asset

The main SQL asset is maintained under:

`02_SQL/swiftcart_sql`

Supporting Python scripts are maintained under:

`02_SQL/Python_scripts`

## 8. Important Note

This document describes the role of the SQL layer and its relationship to the BI model. The actual SQL script remains the source of truth for the exact SQL statements, table definitions, and implementation details.
