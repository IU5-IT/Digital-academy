SELECT sale_date, count(*)
FROM sales
GROUP BY sale_date
HAVING count(*) > 186000;
