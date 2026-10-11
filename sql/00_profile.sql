SELECT 'customers' file,COUNT(*) raw_rows FROM raw_customers UNION ALL SELECT 'orders',COUNT(*) FROM raw_orders UNION ALL SELECT 'order_items',COUNT(*) FROM raw_order_items;
