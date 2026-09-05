# SQL Database Checks

Run against `shop.db` with SQLite after creating test data.

| # | Query | Verification |
|---|---|---|
| 1 | `SELECT * FROM users;` | All persisted users and field values. |
| 2 | `SELECT id, email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;` | Unique email rule; result must be empty. |
| 3 | `SELECT * FROM users WHERE age < 18 OR age > 100;` | No invalid ages persisted. |
| 4 | `SELECT * FROM products;` | Complete product catalog. |
| 5 | `SELECT * FROM products WHERE stock = 0;` | Out-of-stock products. |
| 6 | `SELECT * FROM products WHERE price <= 0 OR stock < 0;` | No invalid price/inventory persisted. |
| 7 | `SELECT * FROM orders WHERE user_id = 1;` | Orders belonging to user 1. |
| 8 | `SELECT o.* FROM orders o LEFT JOIN users u ON u.id=o.user_id WHERE u.id IS NULL;` | No orphan orders by user. |
| 9 | `SELECT o.* FROM orders o LEFT JOIN products p ON p.id=o.product_id WHERE p.id IS NULL;` | No orphan orders by product. |
| 10 | `SELECT o.id, o.total_price, ROUND(o.quantity*p.price,2) expected FROM orders o JOIN products p ON p.id=o.product_id WHERE o.total_price != ROUND(o.quantity*p.price,2);` | Detect incorrect totals when product price has not changed. |
