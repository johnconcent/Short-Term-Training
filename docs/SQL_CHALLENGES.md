# 60 business challenges

Q01–Q10 operate on raw TEXT tables. Q11 onward operate on your cleaned tables, with your completed-sale line view named sales. In Python exercises query IDs remain stable for traceability. Write SQL yourself before asking AI; annotate every AI change. For every answer submit query/code, output, grain, validation and a business interpretation.

## Week 1

**Q01.** Count raw rows in each of the six files before any joins.

**Q02.** Find repeated customer_id values and distinguish exact repeats from conflicting versions.

**Q03.** Find repeated order_id values.

**Q04.** Find repeated line_id values.

**Q05.** Find missing customer references in orders.

**Q06.** Find orders referencing nonblank customer IDs absent from the raw customer table.

**Q07.** Identify invalid calendar dates and dates after the 2025-12-31 extract cutoff.

**Q08.** Find invalid numeric values in line quantity, discount and historical cost.

**Q09.** Identify category/status normalization and missing category issues.

**Q10.** Find orphan product, rep and region references and quantify cascaded exclusions.

## Week 2

**Q11.** Count cleaned orders by status.

**Q12.** Count completed orders in each month, including months with zero orders.

**Q13.** List the ten highest priced cleaned line items with a stable tie-break.

**Q14.** How many customers are in each region, including prospects?

**Q15.** Which products have catalog unit cost above $50?

**Q16.** Calculate annual net revenue from completed retained lines.

**Q17.** Calculate net revenue by month.

**Q18.** Calculate sold units by category.

**Q19.** Find categories with annual revenue above $100000.

**Q20.** What fraction of cleaned orders are cancelled?

## Week 3

**Q21.** Calculate revenue and profit by customer region.

**Q22.** Find customers with no completed retained sale.

**Q23.** Rank the ten customers with highest revenue.

**Q24.** Find products sold in more than 100 distinct completed orders.

**Q25.** Calculate average order value.

**Q26.** Calculate completed order revenue, with one row per order.

**Q27.** Calculate revenue per sales rep, retaining reps with zero sales.

**Q28.** Find customers buying more than three distinct categories.

**Q29.** Calculate revenue share by customer segment.

**Q30.** Find customers whose last completed retained sale was more than 90 days before 2025-12-31; include never-buyers separately.

## Week 4

**Q31.** Compute monthly gross profit and gross margin percentage.

**Q32.** Calculate month-over-month revenue change and growth.

**Q33.** Calculate a rolling three-month revenue total.

**Q34.** Find the top three products in each region by revenue; return exactly three using product_id tie-break.

**Q35.** Show each customer’s prior completed order date, excluding multiple lines in the same order.

**Q36.** Compute days between consecutive completed customer orders.

**Q37.** Calculate cumulative monthly revenue for 2025.

**Q38.** What proportion of annual revenue comes from the top 20 customers?

**Q39.** Which reps are below the average rep revenue in their assigned region, including zero-sales reps?

**Q40.** Find customer-months with three consecutive month-over-month revenue declines; include zero-sales months.

## Week 5

**Q41.** Reconcile revenue from sales detail and an order-level aggregation.

**Q42.** Demonstrate why summing order-level revenue after joining it back to line detail overcounts.

**Q43.** Calculate revenue, COGS, profit and margin by category.

**Q44.** Find product-month groups with gross margin below 20%.

**Q45.** Compute quarterly revenue, profit and margin.

**Q46.** Quantify promotional samples’ revenue, COGS and profit.

**Q47.** How many cleaned completed orders have no retained valid lines?

**Q48.** Produce a product dimension with one row per product, including products never sold.

**Q49.** Produce a date dimension for every day of 2025, including month and quarter.

**Q50.** Produce a completed-sale line-grain fact export with keys and numeric measures.

## Week 6

**Q51.** Independently reproduce annual revenue and profit in Python and reconcile to SQL.

**Q52.** Reproduce monthly revenue in Pandas and compare every month to SQL.

**Q53.** Profile the raw files in Python, including blank IDs and exact duplicates.

**Q54.** Write a Python quality report with invalid dates and distinct reasons per excluded key.

**Q55.** Quantify how the canonical cleaning policy changes revenue versus a naive raw inner join.

**Q56.** Compare Q3 and Q4 realized unit revenue and unit historical cost.

**Q57.** Measure top-20 customer concentration separately in Q1 and Q4.

**Q58.** Identify ten products with largest Q4 gross-profit decline versus Q3.

**Q59.** Challenge an AI query that uses AVG(line profit / line revenue) for company margin.

**Q60.** Write a 300-word executive recommendation supported by three reconciled measures.
