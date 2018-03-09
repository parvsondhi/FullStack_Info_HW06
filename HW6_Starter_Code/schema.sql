-- Insert code to create Database Schema
-- This will create your .db database file for use

drop table if exists customer;
drop table if exists `order`;
drop table if exists tracker;
drop table if exists address;

create table customer (customer_id primary key, first_name, last_name, company, email, phone);
create table address (id primary key, street_address, city, state, country, zip_code);
create table `order` (order_id primary key, name_of_part, manufacturer_of_part);
create table tracker (address_id, order_id, customer_id);