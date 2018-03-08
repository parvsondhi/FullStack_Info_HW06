-- Insert code to create Database Schema
-- This will create your .db database file for use
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    company TEXT,
    email TEXT,
    phone TEXT
);

CREATE TABLE addresses (
    address_id INTEGER PRIMARY KEY,
    street TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    zipcode INTEGER
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    part_name TEXT,
    manufacturer TEXT,
    customer_id INTEGER
);
