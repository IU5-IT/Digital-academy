SElECT surname, COUNT(surname)
FROM customers
WHERE surname is not null
GROUP BY surname;
