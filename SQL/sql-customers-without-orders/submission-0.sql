-- Write your query below
Select customers.name from customers
LEFT JOIN orders on customers.id = orders.customer_id
Where orders.id IS NULL