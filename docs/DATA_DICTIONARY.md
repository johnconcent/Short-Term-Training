# Data specification and dictionary

Files: UTF-8 CSV, comma delimiter, header row, ISO YYYY-MM-DD dates, decimal point, USD. Raw ingestion keeps every field as TEXT to preserve blanks and malformed values. Suggested analytical types below apply only after validation. The row counts describe the delivered raw extracts, including defects; they do not disclose defect locations.

## regions.csv

Raw rows: 4. One region record; region_id is the key.

region_id: integer business key; region_name: text service region.

Expected clean declaration: `region_id INTEGER, region_name TEXT`.

## sales_reps.csv

Raw rows: 8. One rep record; rep_id is the key.

rep_id: integer business key; rep_name: synthetic text; region_id: integer FK to regions.

Expected clean declaration: `rep_id INTEGER, rep_name TEXT, region_id INTEGER`.

## customers.csv

Raw rows: 123. One registered business; customer_id should be unique.

customer_id: integer business key; customer_name: synthetic text; region_id: integer FK; segment: Small/Medium/Enterprise; signup_date: date. A customer can have no purchases.

Expected clean declaration: `customer_id INTEGER, customer_name TEXT, region_id INTEGER, segment TEXT, signup_date TEXT`.

## products.csv

Raw rows: 24. One catalog product; product_id should be unique.

product_id: integer business key; sku: text SKU; product_name: synthetic text; category: text; unit_cost: nonnegative decimal current catalog cost in USD/unit.

Expected clean declaration: `product_id INTEGER, sku TEXT, product_name TEXT, category TEXT, unit_cost REAL`.

## orders.csv

Raw rows: 2402. One order header; order_id should be unique.

order_id: integer business key; customer_id: mandatory customer FK; rep_id: mandatory rep FK; order_date: valid date at or before extract cutoff; status: Completed/Cancelled/Pending.

Expected clean declaration: `order_id INTEGER, customer_id INTEGER, rep_id INTEGER, order_date TEXT, status TEXT`.

## order_items.csv

Raw rows: 6108. One order line; line_id should be unique. Multiple lines per order are normal.

line_id: integer business key; order_id: mandatory order FK; product_id: mandatory product FK; quantity: positive integer units; unit_price: nonnegative USD/unit; discount_pct: decimal fraction [0,1]; unit_cost_at_sale: nonnegative historical USD/unit; is_promo: integer flag 0/1. Zero-price promotional samples are legitimate.

Expected clean declaration: `line_id INTEGER, order_id INTEGER, product_id INTEGER, quantity INTEGER, unit_price REAL, discount_pct REAL, unit_cost_at_sale REAL, is_promo INTEGER`.

## Join contracts

orders.customer_id → customers.customer_id (many-to-one); orders.rep_id → sales_reps.rep_id; order_items.order_id → orders.order_id; order_items.product_id → products.product_id; customers.region_id and sales_reps.region_id → regions.region_id. Deduplicate parent tables before joins. Check keys and row counts before/after each join; unintended fan-out changes money.

The analytical fact grain is one retained line in a completed order. Use line_id as the fact key and order_id as a degenerate dimension. Keep customer, product, rep, region and date dimensions unique at their keys. Current customer region is used throughout; historical region changes are not available. Do not claim SCD history from this snapshot.

## Required quality report fields

file, business_key, field, rule, observed_value, severity, proposed_action, owner_question, exclusion_reason, detected_at, pipeline_version. Include a separate row-count reconciliation. An apparent anomaly is not proof that a value is wrong; accuracy requires external ground truth.
