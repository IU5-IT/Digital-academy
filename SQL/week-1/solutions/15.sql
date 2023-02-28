SELECT DISTINCT customer_id
FROM sales
WHERE sale_date BETWEEN '2020-02-01' AND '2020-02-29'
ORDER BY customer_id DESC;
