# First Power BI assignment — CFO profitability review

## Client request

“Show whether growth is profitable, which regions/products/customer segments deserve attention, and whether missing or rejected records undermine the conclusion.” Submit three report pages and a reproducible model. Visual polish cannot compensate for incorrect totals.

## Model and exports

From your cleaned database export FactSales at one completed retained line per row: line_id, order_id, order_date, customer_id, product_id, rep_id, region_id, quantity, is_promo, revenue, cogs, profit. Also export FactOrders at one cleaned order per row with order_id, order_date, customer_id, rep_id, status. Export DimCustomer, DimProduct, DimRep, DimRegion and DimDate (365 days in 2025). Export a separate QualitySummary with file, raw_rows, exact_duplicate_rows, quarantined_rows and retained_rows. Duplicate removals and nonduplicate quarantines must be disjoint.

Set IDs to whole number, dates to Date, monetary measures to decimal number, rates to decimal number. Define many-to-one, single-direction relationships from each fact to applicable dimensions; mark DimDate as date table. Do not relate FactOrders directly to FactSales. DimRegion relates to FactSales using customer region; avoid also linking DimCustomer to DimRegion and creating two active paths. The cancellation visual uses FactOrders and date/status scope; product/category filters should not imply a category cancellation rate because order headers do not contain category.

## Core DAX to implement and explain

```dax
Net Revenue = SUM(FactSales[revenue])
COGS = SUM(FactSales[cogs])
Gross Profit = [Net Revenue] - [COGS]
Gross Margin % = DIVIDE([Gross Profit], [Net Revenue])
Completed Sale Orders = DISTINCTCOUNT(FactSales[order_id])
Buying Customers = DISTINCTCOUNT(FactSales[customer_id])
Average Order Value = DIVIDE([Net Revenue], [Completed Sale Orders])
Clean Orders = COUNTROWS(FactOrders)
Cancelled Orders = CALCULATE([Clean Orders], FactOrders[status] = "Cancelled")
Cancellation Rate = DIVIDE([Cancelled Orders], [Clean Orders])
Prior Month Revenue = CALCULATE([Net Revenue], DATEADD(DimDate[date], -1, MONTH))
MoM Growth % = DIVIDE([Net Revenue] - [Prior Month Revenue], [Prior Month Revenue])
```

Disable status slicer interaction for the cancellation-rate visual, or explicitly remove status filters in its denominator and document that choice. Use month start/date or a YearMonth key sorted chronologically. Validate January MoM is blank and partial-period filters do not create misleading comparisons. A full-calendar prior-month measure can still be misleading if a slicer selects partial days: label scope and test it.

## Page 1 — Executive overview

Cards: net revenue, gross profit, gross margin, completed-sale orders, buying customers and AOV. Monthly trend: revenue and gross margin, with clear units/axes. Date and region slicers. Three-sentence narrative: finding, recommended action and limitation. Every headline ties to a SQL query ID.

## Page 2 — Margin diagnosis

Revenue/profit/margin by category and product; Q3/Q4 comparison; customer concentration; promotional-cost breakdown. Drill-through or detail table for one product. Identify three investigation candidates, quantify their importance and avoid declaring aggregate mix changes to be a pricing effect. Show Unknown category instead of hiding it.

## Page 3 — Trust and operations

Raw-to-retained counts by file, exclusions and reason summary, refresh/extract date, unresolved owner questions, cancellation rate by month. State that quality counts refer to the full extract and do not respond to sales slicers unless a validated row-level quality model is built. Explain that synthetic data cannot establish real customer profitability or business causality.

## Required verification

Save dashboard/reconciliation.csv with metric, filter_scope, SQL_value, BI_value, absolute_difference, tolerance and status. Check annual revenue/COGS/profit, all twelve monthly revenues, region totals, category totals, distinct orders/customers, promo cost and cancellation rate. Money tolerance $0.01, counts exact, rate tolerance 1e-8. Compare underlying values before displayed rounding. Test one month+region, one category, Unknown, promotional lines and a no-data selection. State which filters affect each fact.

Submit the PBIX, three screenshots, model screenshot, measure definitions, refresh instructions and the reconciliation file. No paid publishing or web service is required. Do not use Publish to web for real data. This package supplies an implementation assignment, not a completed PBIX.
