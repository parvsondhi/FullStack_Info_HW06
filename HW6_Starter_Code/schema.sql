-- Insert code to create Database Schema
-- This will create your .db database file for use

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    company TEXT,
    email TEXT,
    phone TEXT
);

DROP TABLE IF EXISTS address;
CREATE TABLE address (
    id INTEGER PRIMARY KEY,
    street_address TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    zip_code TEXT,
    customer_id INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    name_of_part TEXT,
    manufacturer_of_part TEXT
);

DROP TABLE IF EXISTS cust_orders;
CREATE TABLE cust_orders (
    customer_id INTEGER,
    order_id INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customer(id),
    FOREIGN KEY(order_id) REFERENCES orders(id)
);

DROP VIEW IF EXISTS cust_address;
CREATE VIEW cust_address AS
    SELECT *
    FROM customers
    LEFT JOIN address ON customers.id=address.customer_id
    ;
