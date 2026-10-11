# Client engagement brief

**Client:** Cumberland Business Supply, a fictional regional B2B distributor. **Sponsor:** CFO. **Users:** VP Sales, regional managers and purchasing lead. **Decision:** identify margin risks and choose three actions for next quarter. **Scope:** January–December 2025 orders and order lines in USD. There is no prior-year dataset, inventory ledger, customer support data or return feed.

## Questions to clarify in Week 1

What counts as a sale? How are discounts applied? Does “customer” mean a registered business or an active buyer? Can zero-dollar orders be legitimate? Which region owns revenue? How should unknown categories be reported? What happens to lines whose parent order is unusable? Does “profit” include operating costs? How much excluded data could change a recommendation?

## Agreed metric contract

- Sales metrics use **Completed** orders with at least one retained valid line. Cancelled and Pending orders do not generate recognized sales in this exercise.
- Line net revenue = quantity × unit_price × (1 − discount_pct). Discount is a fraction from 0 to 1. USD, no sales tax, freight or currency conversion.
- Line COGS = quantity × unit_cost_at_sale. Catalog product cost is for reference; use historical line cost in profitability.
- Gross profit = net revenue − COGS. Gross margin = SUM(gross profit) / SUM(net revenue). Zero denominator yields blank/NULL. This is gross profit, not operating profit.
- Average order value = retained completed-sale revenue / distinct retained completed-sale order_id. A completed order with no valid lines must be separately reported, not treated as a trustworthy zero-dollar order.
- Buying customer count = distinct customer_id in completed retained sales. Registered customers include prospects.
- Cancellation rate = cancelled cleaned orders / all cleaned orders. The denominator includes Pending. Keep a separate cleaned order table for this measure.
- Region attribution uses the customer region. Rep comparisons use each rep's assigned region. Do not assume those are interchangeable.
- Inactivity = last completed retained sale more than 90 days before 2025-12-31. Never-buyers receive a separate label.
- Promotional lines have is_promo=1 and zero price; they retain their cost and may have negative gross profit. Returns are not represented. Negative quantities are invalid in this feed.
- Unknown product category stays Unknown; never infer its label from the product ID. One year of data does not support YoY analysis or a causal seasonal claim.

## Cleaning agreement

Preserve raw extracts. Remove exact duplicate records, recording the removal. Conflicting duplicate keys require investigation and quarantine rather than arbitrary first/last selection. Trim/title-case category and status. Map blank category to Unknown. Quarantine records with missing/unknown mandatory keys, invalid/future dates, nonpositive quantities, out-of-range discounts or negative costs. Cascade unusable customer exclusions to orders and unusable orders to lines. Do not fabricate source corrections. Retain all exclusion reasons but count each excluded row once.

Record raw→deduplicated→quarantined→retained counts for every table, with normalization counts separately. A row can have multiple defect reasons. Business totals on the cleaned subset are provisional; the excluded records have not been resolved by the source owner. Explain how the loss of customers/transactions could bias conclusions.

## Final client acceptance

One reproducible pipeline; 60 exercises; line-grain fact and conformed dimensions; three-page dashboard; reconciled financial totals; 300-word executive memo; 10-minute presentation with three evidence-backed actions and named owners. No claim of forecasting accuracy or churn prediction without labels and validation.
