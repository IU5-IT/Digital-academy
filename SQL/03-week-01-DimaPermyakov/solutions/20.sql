SELECT EXTRACT(MONTH FROM sale_date) as month, count(*)
FROM sales
WHERE EXTRACT(YEAR FROM sale_date) = '2020'
GROUP BY month;
