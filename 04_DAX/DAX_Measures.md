# SwiftCart BI — DAX Measures

This document records the confirmed measures in `Measures_Table`.
Descriptions are kept brief and reflect the measure names/use confirmed during the project.
Exact DAX expressions are intentionally not reproduced here because the formulas were not extracted directly.

## Revenue

| Measure | Purpose |
|---|---|
| Net Revenue | Revenue metric after applicable adjustments. |
| Total Revenue | Overall revenue measure. |
| Category Revenue | Revenue used for category-level analysis. |
| Revenue Online | Revenue associated with online orders/channel analysis. |
| Revenue All Customers | Revenue across the customer population. |

## Time Intelligence

| Measure | Purpose |
|---|---|
| Revenue LY | Revenue for the comparable previous-year period. |
| Revenue MTD | Revenue month-to-date. |
| Revenue YTD | Revenue year-to-date. |
| Revenue YoY % | Year-over-year revenue percentage change. |
| Revenue Rolling 30D | Revenue over a rolling 30-day period. |

## Performance

| Measure | Purpose |
|---|---|
| Total Profit | Overall profit measure. |
| Profit margin % | Profitability expressed as a percentage. |
| Total Discount | Total discount amount. |
| Average Order Value | Average revenue/value per order. |
| Total Quantity | Total quantity sold. |
| Total Orders | Total order count. |

## Ranking

| Measure | Purpose |
|---|---|
| Revenue Rank | Revenue-based ranking measure. |
| Top 10 City Revenue | Revenue analysis for the top 10 cities. |
| Top 10 Customer Revenue | Revenue analysis for the top 10 customers. |
| Top 10 Product Revenue | Revenue analysis for the top 10 products. |

## Customer

| Measure | Purpose |
|---|---|
| High Value Customer | Identifies/flags high-value customer performance. |

## Display Folders

The measures are organized in Power BI under:

- `Revenue`
- `Time Intelligence`
- `Performance`
- `Ranking`
- `Customer`

## Note

The Power BI report remains the source of truth for the actual DAX expressions. This document is an inventory and quick-reference guide, not a replacement for the measures in the `.pbix` file.
