-- Insert code to create Database Schema
-- This will create your .db database file for use

drop table if exists customers;

CREATE TABLE customers(
	customer_id integer PRIMARY KEY,
	first_name text not null,
	last_name text not null,
	company text not null,
	email text not null,
	phone char not null 
);



drop table if exists addresses;

CREATE TABLE addresses(
	id integer,
	street_address text not null,
	state_ text not null,
	country text not null,
	zip_code text not null,
    FOREIGN KEY (id) REFERENCES customers(customer_id)
	CONSTRAINT PK_Address PRIMARY KEY (sreet_address, state_, country, zip_code))
);


drop table if exists orders;
	
CREATE TABLE orders(
	order_id integer PRIMARY KEY,
	name_of_part text not null,
	manufacturer_of_part text not null,
	);



DROP TABLE if exists order_match;

CREATE TABLE order_match(
	id integer PRIMARY KEY,
	order_id integer,
	customer_id integer,	
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
	);
