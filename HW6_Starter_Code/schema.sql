-- -- Insert code to create Database Schema
-- -- This will create your .db database file for use
drop table if exists customer;
CREATE TABLE customer(
	customer_id integer primary key not null,
	firstName text not null,
	lastName text not null,
	company text not null,
	email text not null,
	phone integer not null
);

drop table if exists address;
CREATE TABLE address(
	street_address text not null,
	city text not null,
	state text not null,
	country text not null,
	zip_code integer not null,
	id integer not null,
	FOREIGN KEY (id) REFERENCES customer(customer_id)
);

drop table if exists order_to;
CREATE TABLE order_to(
	order_id integer primary key,
	partName text not null,
	manufacturerName text not null,
	customer_id integer
); 

drop table if exists cus_order;
CREATE TABLE cus_order(
	id integer,
	customer_id integer,	
	order_id integer,
	FOREIGN KEY(order_id) REFERENCES order_to(order_id),
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);