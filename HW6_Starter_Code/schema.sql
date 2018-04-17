-- Insert code to create Database Schema
-- This will create your .db database file for use

drop table if exists customer;
drop table if exists `order`;
drop table if exists tracker;
drop table if exists address;

create table customer (customer_id integer primary key, first_name text not null, last_name text not null, company text not null, email text not null, phone integer);
create table address (address_id primary key, street_address text not null, city text not null, state text not null, country text not null, zip_code integer, customer_id, FOREIGN KEY(customer_id) REFERENCES customer(customer_id));
create table `order` (order_id primary key, name_of_part text not null, manufacturer_of_part text not null);
create table tracker (order_id, customer_id, FOREIGN KEY(order_id) REFERENCES `order`(order_id), FOREIGN KEY(customer_id) REFERENCES customer(customer_id));

