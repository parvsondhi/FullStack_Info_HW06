drop table if exists customers;
create table customers (
	customer_id integer primary key,
	email text not null,
	first_name text not null,
	last_name text not null,
	company text not null,
	phone numeric not null
);

drop table if exists orders;
create table orders (
	order_id integer primary key,
	name_of_part text not null,
	manufacturer_of_part text not null,
	customer_ordered numeric,
	FOREIGN KEY (customer_ordered) REFERENCES customers(customer_id)
);

drop table if exists address;
create table address (
	address_id integer primary key,
	street_address text not null,
	city text not null,
	state text not null,
	country text not null,
	zip_code numeric not null
);



