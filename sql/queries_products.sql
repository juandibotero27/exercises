-- Comments in SQL Start with dash-dash --

products_db=# INSERT INTO products (name, price, can_be_returned) VALUES
products_db-# ('chair', 44.00, false),
products_db-# ('stool', 25.99, true),
products_db-# ('table', 124.00, false)
products_db-# ;


products_db=# SELECT * FROM products;


products_db=# SELECT name FROM products
products_db-# ;


products_db=# SELECT name, price FROM products;

products_db=# INSERT INTO products (name,price,can_be_returned)                                                               VALUES ('ipad',699.00,true);

products_db=# SELECT * FROM products WHERE can_be_returned = true;

products_db=# SELECT * FROM products WHERE price < 44.00;

SELECT * FROM products WHERE  price BETWEEN 22.50 AND 99.99;

products_db=# UPDATE products SET price = price - 20.00;

products_db=# DELETE FROM products WHERE price < 25.00;

products_db=# UPDATE products SET can_be_returned = true

















