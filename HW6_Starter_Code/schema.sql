-- Insert code to create Database Schema
-- This will create your .db database file for use
CREATE TABLE customers (
customer_id INTEGER PRIMARY KEY, 
first_name TEXT, last_name TEXT, company TEXT, email TEXT, phone TEXT
);

CREATE TABLE addresses (
id INTEGER PRIMARY KEY, 
street_address TEXT, city TEXT, state TEXT, country TEXT, zip_code INTEGER
);

CREATE TABLE orders (
order_id INTEGER PRIMARY KEY, part_name TEXT, manufacturer TEXT, customer_id INTEGER
);

CREATE TABLE customer_orders (
order_id INTEGER ,customer_id INTEGER
);

