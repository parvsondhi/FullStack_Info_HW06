select c.company, co.*, o.* FROM customers AS c, customers_orders AS co
LEFT JOIN orders As o ON co.order_id = o.order_id
WHERE c.customer_id = co.customer_id
