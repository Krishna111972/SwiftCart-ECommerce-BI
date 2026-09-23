-- SwiftCart E-Commerce Analytics
-- 01: Data Load & Validation

CREATE DATABASE IF NOT EXISTS ecommerce_analytics;
USE ecommerce_analytics;

-- Enable CSV import
SET GLOBAL local_infile = 1;

-- Cities
DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
    CityKey VARCHAR(10),
    City VARCHAR(50)
);

LOAD DATA LOCAL INFILE 'E:/SwiftCart_BI_Project/01_Raw_Data/cities.csv'
INTO TABLE cities
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Customers
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    CustomerKey VARCHAR(20),
    CustomerName VARCHAR(100),
    Email VARCHAR(150),
    CityKey VARCHAR(10),
    City VARCHAR(50),
    Gender VARCHAR(20),
    AgeGroup VARCHAR(30),
    DateOfBirth VARCHAR(20)
);

LOAD DATA LOCAL INFILE 'E:/SwiftCart_BI_Project/01_Raw_Data/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Products
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    ProductKey VARCHAR(20),
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Subcategory VARCHAR(50),
    SellingPrice DECIMAL(14,2),
    UnitCost DECIMAL(14,2)
);

LOAD DATA LOCAL INFILE 'E:/SwiftCart_BI_Project/01_Raw_Data/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Warehouses
DROP TABLE IF EXISTS warehouses;
CREATE TABLE warehouses (
    WarehouseKey VARCHAR(20),
    WarehouseName VARCHAR(100),
    CityKey VARCHAR(10),
    City VARCHAR(50),
    WarehouseSize VARCHAR(20)
);

LOAD DATA LOCAL INFILE 'E:/SwiftCart_BI_Project/01_Raw_Data/warehouses.csv'
INTO TABLE warehouses
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Riders
DROP TABLE IF EXISTS riders;
CREATE TABLE riders (
    RiderKey VARCHAR(20),
    RiderName VARCHAR(100),
    CityKey VARCHAR(10),
    City VARCHAR(50),
    EmploymentType VARCHAR(30),
    VehicleType VARCHAR(30)
);

LOAD DATA LOCAL INFILE 'E:/SwiftCart_BI_Project/01_Raw_Data/riders.csv'
INTO TABLE riders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Orders
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    OrderID VARCHAR(20),
    OrderDate DATE,
    CustomerKey VARCHAR(20),
    WarehouseKey VARCHAR(20),
    RiderKey VARCHAR(20),
    OrderStatus VARCHAR(20),
    PaymentMethod VARCHAR(30),
    OrderChannel VARCHAR(30),
    NumberOfLines INT,
    OrderAmount DECIMAL(14,2),
    DiscountAmount DECIMAL(14,2),
    DeliveryFee DECIMAL(14,2),
    TaxAmount DECIMAL(14,2),
    TotalAmount DECIMAL(14,2)
);

LOAD DATA LOCAL INFILE 'E:/SwiftCart_BI_Project/01_Raw_Data/orders.csv'
INTO TABLE orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    OrderID,
    @OrderDate,
    CustomerKey,
    WarehouseKey,
    RiderKey,
    OrderStatus,
    PaymentMethod,
    OrderChannel,
    NumberOfLines,
    OrderAmount,
    DiscountAmount,
    DeliveryFee,
    TaxAmount,
    TotalAmount
)
SET OrderDate = STR_TO_DATE(@OrderDate, '%m/%d/%Y');

-- Order Items
DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
    OrderItemID VARCHAR(20),
    OrderID VARCHAR(20),
    ProductKey VARCHAR(20),
    Quantity INT,
    UnitPrice DECIMAL(12,2),
    UnitCost DECIMAL(12,2),
    GrossAmount DECIMAL(14,2),
    DiscountAmount DECIMAL(14,2),
    NetAmount DECIMAL(14,2),
    CostAmount DECIMAL(14,2),
    ProfitAmount DECIMAL(14,2)
);

LOAD DATA LOCAL INFILE 'E:/SwiftCart_BI_Project/01_Raw_Data/order_items.csv'
INTO TABLE order_items
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Row counts
SELECT 'cities' AS table_name, COUNT(*) AS row_count FROM cities
UNION ALL SELECT 'customers', COUNT(*) FROM customers
UNION ALL SELECT 'products', COUNT(*) FROM products
UNION ALL SELECT 'orders', COUNT(*) FROM orders
UNION ALL SELECT 'order_items', COUNT(*) FROM order_items
UNION ALL SELECT 'riders', COUNT(*) FROM riders
UNION ALL SELECT 'warehouses', COUNT(*) FROM warehouses;

-- Key validation
SELECT COUNT(*) total_rows,
       COUNT(DISTINCT CustomerKey) unique_keys,
       SUM(CustomerKey IS NULL OR CustomerKey = '') missing_keys
FROM customers;

SELECT COUNT(*) total_rows,
       COUNT(DISTINCT ProductKey) unique_keys,
       SUM(ProductKey IS NULL OR ProductKey = '') missing_keys
FROM products;

SELECT COUNT(*) total_rows,
       COUNT(DISTINCT OrderID) unique_keys,
       SUM(OrderID IS NULL OR OrderID = '') missing_keys
FROM orders;

SELECT COUNT(*) total_rows,
       COUNT(DISTINCT OrderItemID) unique_keys,
       SUM(OrderItemID IS NULL OR OrderItemID = '') missing_keys
FROM order_items;

SELECT COUNT(*) total_rows,
       COUNT(DISTINCT RiderKey) unique_keys,
       SUM(RiderKey IS NULL OR RiderKey = '') missing_keys
FROM riders;

SELECT COUNT(*) total_rows,
       COUNT(DISTINCT WarehouseKey) unique_keys,
       SUM(WarehouseKey IS NULL OR WarehouseKey = '') missing_keys
FROM warehouses;

SELECT COUNT(*) total_rows,
       COUNT(DISTINCT CityKey) unique_keys,
       SUM(CityKey IS NULL OR CityKey = '') missing_keys
FROM cities;

-- SwiftCart E-Commerce Analytics
-- 02: Business Analysis

-- 1. Total Revenue
SELECT
    ROUND(SUM(TotalAmount), 2) AS total_revenue
FROM orders;
-- 2. Total Profit
SELECT
    ROUND(SUM(ProfitAmount), 2) AS total_profit
FROM order_items;
-- 3. Total Orders
SELECT
    COUNT(*) AS total_orders
FROM orders;
-- 4. Total Customers
SELECT
    COUNT(DISTINCT CustomerKey) AS total_customers
FROM orders;
-- 5. Average Order Value
SELECT
    ROUND(AVG(TotalAmount), 2) AS average_order_value
FROM orders;
-- 6. Total Quantity Sold
SELECT
    SUM(Quantity) AS total_quantity_sold
FROM order_items;
-- 7. Total Discount
SELECT
    ROUND(SUM(DiscountAmount), 2) AS total_discount
FROM orders;

-- 8. Total Delivery Fee
SELECT
    ROUND(SUM(DeliveryFee), 2) AS total_delivery_fee
FROM orders;

-- 9. Total Tax
SELECT
    ROUND(SUM(TaxAmount), 2) AS total_tax
FROM orders;

-- 10. Total Gross Sales
SELECT
    ROUND(SUM(GrossAmount), 2) AS total_gross_sales
FROM order_items;

-- 11. Total Net Sales
SELECT
    ROUND(SUM(NetAmount), 2) AS total_net_sales
FROM order_items;

-- 12. Total Cost
SELECT
    ROUND(SUM(CostAmount), 2) AS total_cost
FROM order_items;

-- 13. Profit Margin
SELECT
    ROUND(
        SUM(ProfitAmount) / SUM(NetAmount) * 100,
        2
    ) AS profit_margin_pct
FROM order_items;

-- 14. Orders by Status
SELECT
    OrderStatus,
    COUNT(*) AS total_orders
FROM orders
GROUP BY OrderStatus
ORDER BY total_orders DESC;

-- 15. Revenue by Payment Method
SELECT
    PaymentMethod,
    ROUND(SUM(TotalAmount), 2) AS revenue
FROM orders
GROUP BY PaymentMethod
ORDER BY revenue DESC;

-- 16. Revenue by Order Channel
SELECT
    OrderChannel,
    ROUND(SUM(TotalAmount), 2) AS revenue
FROM orders
GROUP BY OrderChannel
ORDER BY revenue DESC;

-- 17. Revenue by City
SELECT
    c.City,
    ROUND(SUM(o.TotalAmount), 2) AS revenue
FROM orders o
JOIN customers c
    ON o.CustomerKey = c.CustomerKey
GROUP BY c.City
ORDER BY revenue DESC;

-- 18. Revenue by Category
SELECT
    p.Category,
    ROUND(SUM(oi.NetAmount), 2) AS revenue
FROM order_items oi
JOIN products p
    ON oi.ProductKey = p.ProductKey
GROUP BY p.Category
ORDER BY revenue DESC;

-- 19. Profit by Category
SELECT
    p.Category,
    ROUND(SUM(oi.ProfitAmount), 2) AS profit
FROM order_items oi
JOIN products p
    ON oi.ProductKey = p.ProductKey
GROUP BY p.Category
ORDER BY profit DESC;

-- 20. Top 10 Products by Revenue
SELECT
    p.ProductName,
    ROUND(SUM(oi.NetAmount), 2) AS revenue
FROM order_items oi
JOIN products p
    ON oi.ProductKey = p.ProductKey
GROUP BY p.ProductKey, p.ProductName
ORDER BY revenue DESC
LIMIT 10;

-- 21. Top 10 Products by Profit
SELECT
    p.ProductName,
    ROUND(SUM(oi.ProfitAmount), 2) AS profit
FROM order_items oi
JOIN products p
    ON oi.ProductKey = p.ProductKey
GROUP BY p.ProductKey, p.ProductName
ORDER BY profit DESC
LIMIT 10;

-- 22. Monthly Revenue
SELECT
    DATE_FORMAT(OrderDate, '%Y-%m') AS month,
    ROUND(SUM(TotalAmount), 2) AS revenue
FROM orders
GROUP BY DATE_FORMAT(OrderDate, '%Y-%m')
ORDER BY month;

-- 23. Monthly Orders
SELECT
    DATE_FORMAT(OrderDate, '%Y-%m') AS month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY DATE_FORMAT(OrderDate, '%Y-%m')
ORDER BY month;

-- 24. Revenue by Warehouse
SELECT
    w.WarehouseName,
    ROUND(SUM(o.TotalAmount), 2) AS revenue
FROM orders o
JOIN warehouses w
    ON o.WarehouseKey = w.WarehouseKey
GROUP BY w.WarehouseKey, w.WarehouseName
ORDER BY revenue DESC;

-- 25. Revenue by Rider
SELECT
    r.RiderName,
    COUNT(o.OrderID) AS total_orders,
    ROUND(SUM(o.TotalAmount), 2) AS revenue
FROM orders o
JOIN riders r
    ON o.RiderKey = r.RiderKey
GROUP BY r.RiderKey, r.RiderName
ORDER BY revenue DESC
LIMIT 10;

-- 26. Customer Revenue
SELECT
    c.CustomerName,
    COUNT(o.OrderID) AS total_orders,
    ROUND(SUM(o.TotalAmount), 2) AS revenue
FROM orders o
JOIN customers c
    ON o.CustomerKey = c.CustomerKey
GROUP BY c.CustomerKey, c.CustomerName
ORDER BY revenue DESC
LIMIT 10;

-- 27. Repeat Customers
SELECT
    COUNT(*) AS repeat_customers
FROM (
    SELECT CustomerKey
    FROM orders
    GROUP BY CustomerKey
    HAVING COUNT(*) > 1
) x;

-- 28. Average Orders per Customer
SELECT
    ROUND(
        COUNT(*) / COUNT(DISTINCT CustomerKey),
        2
    ) AS avg_orders_per_customer
FROM orders;

-- 29. Average Profit per Order
SELECT
    ROUND(
        SUM(ProfitAmount) / COUNT(DISTINCT OrderID),
        2
    ) AS avg_profit_per_order
FROM order_items;

-- 30. Category Quantity Sold
SELECT
    p.Category,
    SUM(oi.Quantity) AS quantity_sold
FROM order_items oi
JOIN products p
    ON oi.ProductKey = p.ProductKey
GROUP BY p.Category
ORDER BY quantity_sold DESC;

-- Advanced SQL Analysis

-- 31. Rank Products by Revenue
SELECT
    p.ProductName,
    ROUND(SUM(oi.NetAmount), 2) AS revenue,
    RANK() OVER (
        ORDER BY SUM(oi.NetAmount) DESC
    ) AS revenue_rank
FROM order_items oi
JOIN products p
    ON oi.ProductKey = p.ProductKey
GROUP BY p.ProductKey, p.ProductName;

-- 32. Rank Customers by Revenue
SELECT
    c.CustomerName,
    ROUND(SUM(o.TotalAmount), 2) AS revenue,
    RANK() OVER (
        ORDER BY SUM(o.TotalAmount) DESC
    ) AS customer_rank
FROM orders o
JOIN customers c
    ON o.CustomerKey = c.CustomerKey
GROUP BY c.CustomerKey, c.CustomerName;

-- 33. Monthly Revenue with Previous Month
WITH monthly_sales AS (
    SELECT
        DATE_FORMAT(OrderDate, '%Y-%m') AS month,
        SUM(TotalAmount) AS revenue
    FROM orders
    GROUP BY DATE_FORMAT(OrderDate, '%Y-%m')
)
SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(
        LAG(revenue) OVER (ORDER BY month),
        2
    ) AS previous_month_revenue
FROM monthly_sales
ORDER BY month;

-- 34. Running Revenue
WITH monthly_sales AS (
    SELECT
        DATE_FORMAT(OrderDate, '%Y-%m') AS month,
        SUM(TotalAmount) AS revenue
    FROM orders
    GROUP BY DATE_FORMAT(OrderDate, '%Y-%m')
)
SELECT
    month,
    ROUND(revenue, 2) AS monthly_revenue,
    ROUND(
        SUM(revenue) OVER (ORDER BY month),
        2
    ) AS running_revenue
FROM monthly_sales
ORDER BY month;

-- 35. Customer Segmentation
SELECT
    CustomerKey,
    COUNT(*) AS total_orders,
    ROUND(SUM(TotalAmount), 2) AS revenue,
    CASE
        WHEN SUM(TotalAmount) >= 10000 THEN 'High Value'
        WHEN SUM(TotalAmount) >= 5000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS customer_segment
FROM orders
GROUP BY CustomerKey
ORDER BY revenue DESC;