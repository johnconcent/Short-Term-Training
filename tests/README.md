# Meaningful validation checklist

Implement checks for unique dimension keys and line IDs, orphan FKs after cleaning, valid dates/discounts/costs, 365 contiguous date keys, raw-to-retained counts, revenue−COGS=profit and annual=sum(months). Demonstrate one failure using a temporary duplicate parent row, then restore the data and show it passes. Do not merely assert the pipeline's own output is equal to itself.

Validate same inputs with an independent aggregation or Python calculation. Check AOV distinct order denominator and margin ratio-of-sums. Record tolerances and excluded records. Tests should fail clearly when the fixture violates the business contract.
