-- Insert code to create Database Schema
-- This will create your .db database file for use
DROP TABLE customer;
DROP TABLE address;
DROP TABLE orders;
DROP TABLE customer_orders;


CREATE TABLE customer(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    company TEXT,
    email TEXT,
    phone TEXT
);

CREATE TABLE address(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    street_address TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    zip_code INTEGER,
    customer_id INTEGER
);

CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_of_part TEXT,
    manufacturer_of_part TEXT
);

CREATE TABLE customer_orders(
    order_id INTEGER,
    customer_id INTEGER
);