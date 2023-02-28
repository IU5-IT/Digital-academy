SELECT product_id, store_id
FROM sales
WHERE customer_id IS NOT NULL AND sale_date = '2020-02-14';
