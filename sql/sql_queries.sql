
-- QUESTION 1: Monthly Sales
-- Calculate total sales for each month.

SELECT
    strftime('%Y-%m', date) AS month,
    SUM(amount) AS total_sales
FROM transactions
GROUP BY month
ORDER BY month;


-- QUESTION 2: Top Product Categories
-- Find which product categories generate the most revenue.

SELECT
    category,
    SUM(amount) AS total_sales
FROM transactions
GROUP BY category
ORDER BY total_sales DESC;


-- QUESTION 3: Average Spend Per Customer
-- Calculate the average transaction amount for each customer.

SELECT
    customer_id,
    ROUND(AVG(amount), 2) AS average_spend,
    COUNT(*) AS total_transactions
FROM transactions
GROUP BY customer_id
ORDER BY average_spend DESC;
