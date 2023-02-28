# Tasks

```SQL
-- 1. Выберите все адреса магазинов, которые хранятся в БД.
SELECT address 
FROM stores;

-- 2. Выберите все уникальные номера регионов магазинов.
SELECT DISTINCT region 
FROM stores;

-- 3. Выберите все уникальные сочетания имя-фамилия зарегистрированных клиентов.
SELECT DISTINCT name, surname 
FROM customers;

-- 4. Мы хотим создать карту, в какие магазины ходит каждый конкретный покупатель. Выберите все пары 
-- customer_id, store_id для этого.
SELECT customer_id, store_id
FROM sales;

-- 5. Выведите все уникальные бренды товаров в алфавитном порядке.
SELECT DISTINCT brand
FROM products
ORDER BY brand;

-- 6. Мы хотим оценить, какой объем персональных предложений планировать на следующий год. Выведите customer_id и 
-- дату рождения клиентов, отсортированные по дате рождения без учета года (от 1 января до 31 декабря).
SELECT customer_id, birth_date
FROM customers
ORDER BY EXTRACT(MONTH FROM birth_date), EXTRACT(DAY FROM birth_date);

-- 7. Мы разделили регионы по возрастанию номера региона на тройки, чтобы провести на них проверку бизнес-гипотез.
-- Выведите тертью тройку номеров регионов.
SELECT DISTINCT region
FROM stores
ORDER BY  region
LIMIT 3
OFFSET 5;

-- 8. Выведите самую позднюю дату, на которую хотя бы для одного товара установлена цена. Для решения воспользуйтесь бызовыми операторами.
SELECT start_date
FROM prices
ORDER BY start_date DESC
LIMIT 1;

-- 9. Выведите все уникальные имена клиентов, фамилия которых Джигурда.
SELECT DISTINCT name 
FROM customers
WHERE surname = 'Джигурда'

-- 10. Выведите все уникальные адреса магазинов региона 5 в алфавитном порядке.
SELECT DISTINCT address FROM stores
WHERE region = '5'
ORDER BY address;

-- 11. Выведите все уникальные product_id, которые были проданы покупателю с customer_id = 69 14 февраля 2020 года.
SELECT DISTINCT product_id 
FROM sales
WHERE customer_id = 69 AND sale_date = '2020-02-14';

-- 12. Выведите все пары product_id - store_id, которые купили зарегистрированные пользователи 14 февраля 2020 года.
SELECT product_id, store_id
FROM sales
WHERE customer_id IS NOT NULL AND sale_date = '2020-02-14';

-- 13. Выведите все данные по ценам, которые действовали в течение февраля 2020 года 
-- (учтите оба поля start_date и end_date)
SELECT price
FROM prices
WHERE start_date >= '2020-02-01' AND end_date <= '2020-02-29';

--14. Мы хотим сделать акцию к международному дню буквы К и оценить, сколько покупателей могут праздновать этот день.
-- Выведите все customer_id, имена и фамилии покупателей, у которых имя или фамилия начинаются с буквы К (кириллицей).

SELECT customer_id
FROM customers
WHERE name LIKE 'К%' OR surname LIKE 'К%';

-- 15. Выведите все уникальные customer_id покупателей, которые совершали покупки в феврале 2020 года, 
-- в порядке возрастания.
SELECT DISTINCT customer_id
FROM sales
WHERE sale_date BETWEEN '2020-02-01' AND '2020-02-29'
ORDER BY customer_id DESC;

-- 16. Посчитайте количество магазинов в регионе 5. Выведите единственное число.
SELECT count(*) 
FROM stores
WHERE region = 5;

-- 17. Выведите средннюю цену каждого товара за 2020 год в виде product_id - avg_price,
-- где avg_price - это название колонки со средней ценой. Отсортируйте выборку в порядке возрастания product_id.
SELECT product_id, AVG(price) as avg_price
FROM prices
WHERE EXTRACT(YEAR FROM start_date) = '2020' AND EXTRACT(YEAR FROM end_date) = '2020'
GROUP BY product_id
ORDER BY product_id;

-- 18. Мы хотим изучить, в какие дни у нас было больше всего продаж. Выведите пары дата - количество продаж в те дни,
-- когда их было больше 186000.
SELECT sale_date, count(*)
FROM sales
GROUP BY sale_date
HAVING count(*) > 186000;

-- 19. Выведите количество дней, в которые количество продаж было больше 186000.
SELECT count(*) FROM
(
    SELECT sale_date, count(*)
    FROM sales
    GROUP BY sale_date
    HAVING count(*) > 186000
) d1;

-- 20. Выведите количество продаж по месяцам в 2020 году. Формат вывода: двузначный номер месяца - количество продаж.
SELECT EXTRACT(MONTH FROM sale_date) as month, count(*)
FROM sales
WHERE EXTRACT(YEAR FROM sale_date) = '2020'
GROUP BY month;

-- 21. Выведите самый популярный product_id среди незарегистрированных клиентов.
SELECT product_id FROM
(
SELECT product_id, COUNT(product_id) as counter
FROM sales
WHERE customer_id IS NULL
GROUP BY product_id
ORDER BY counter DESC
LIMIT 1
) d1;

-- 22. Посчитайте количество однофамильцев для каждой фамилии.
-- Выведите колонки surname, n, где n - это название колонки с количеством людей.
SElECT surname, COUNT(surname)
FROM customers
WHERE surname is not null
GROUP BY surname;
```