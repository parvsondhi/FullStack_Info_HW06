drop table if exists customers;
drop table if exists address;
drop table if exists orders;
drop table if exists customer_to_order;

create table customers(
	customer_id integer primary key,
	first_name text not null,
	last_name text not null,
	company text not null,
	email text not null,
	phone text not null
);

create table address(
	id integer primary key,
	street_address text not null,
	city text not null,
	state text not null,
	country text not null,
	zip_code text not null,
	customer_id integer not null,
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

create table orders(
	order_id integer primary key,
	name_of_part text not null,
	manufacturer_of_part text not null
);

create table customer_to_order(
	id integer primary key,
	order_id integer not null,
	customer_id integer not null,
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
	FOREIGN KEY(order_id) REFERENCES orders(order_id)
);
-- Insert code to create Database Schema
-- This will create your .db database file for use
