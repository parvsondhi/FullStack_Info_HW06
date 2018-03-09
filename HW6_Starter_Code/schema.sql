-- Insert code to create Database Schema
-- This will create your .db database file for use

drop table if exists 'customer';
drop table if exists 'order';
drop table if exists 'orders';
drop table if exists 'address';
drop table if exists 'customer_orders';

CREATE TABLE 'customer' ( 
    customer_id integer primary key,
    first_name text not null, 
    last_name text not null,
    company text not null,
    email text not null,
    phone_number text not null
);

CREATE TABLE `orders` (
	`order_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name_of_part`	TEXT NOT NULL,
	`manufacturer_of_part`	TEXT NOT NULL
);

CREATE TABLE `address` (
	`address_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`street_address`	TEXT NOT NULL,
	`city`	TEXT NOT NULL,
	`state`	TEXT NOT NULL,
	`country`	TEXT NOT NULL,
	`zip_code`	INTEGER NOT NULL,
	'customer_id' INTEGER NOT NULL,
	FOREIGN KEY(`customer_id`) REFERENCES `customer`(`customer_id`)
);

CREATE TABLE `customer_orders` (
	`customer_id`	integer,
	`order_id`	integer,
	FOREIGN KEY(`order_id`) REFERENCES `order`(`order_id`),
	FOREIGN KEY(`customer_id`) REFERENCES `customer`(`customer_id`)
);