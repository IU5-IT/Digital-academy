SELECT product_id FROM
(
SELECT product_id, COUNT(product_id) as counter
FROM sales
WHERE customer_id IS NULL
GROUP BY product_id
ORDER BY counter DESC
LIMIT 1
) d1;
