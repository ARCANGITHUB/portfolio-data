-- Total sales by month
SELECT strftime('%Y-%m', order_date) AS year_month,
       SUM(sales) AS total_sales
FROM sales
GROUP BY year_month
ORDER BY year_month;

-- Average discount and profit by category
SELECT category,
       ROUND(AVG(discount), 3) AS avg_discount,
       ROUND(AVG(profit), 2) AS avg_profit
FROM sales
GROUP BY category
ORDER BY avg_profit DESC;

-- Top 10 most profitable products
SELECT product_name,
       SUM(profit) AS total_profit
FROM sales
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;

-- Sales by region and segment
SELECT region, segment,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit
FROM sales
GROUP BY region, segment
ORDER BY total_sales DESC;

-- Yearly profit margin
SELECT strftime('%Y', order_date) AS year,
       ROUND(SUM(profit) / SUM(sales), 4) * 100 AS profit_margin_percent
FROM sales
GROUP BY year
ORDER BY year;
