-- Insert code to create Database Schema
-- This will create your .db database file for use
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
	customer_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	company TEXT NOT NULL,
	email TEXT NOT NULL,
	phone TEXT NOT NULL
);

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
	address_id INTEGER PRIMARY KEY,
	street_address TEXT NOT NULL,
	city TEXT NOT NULL,
	state TEXT NOT NULL,
	country TEXT NOT NULL,
	zip_code TEXT NOT NULL,
	customer_id INTEGER NOT NULL
	--FOREIGN KEY(customer_id) REFERENCES CUSTOMERS(customer_id)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
	order_id INTEGER PRIMARY KEY,
	name_of_part TEXT NOT NULL,
	manufacturer_of_part TEXT NOT NULL,
	customer_id INTEGER NOT NULL
	--FOREIGN KEY(customer_id) REFERENCES CUSTOMERS(customer_id)
);