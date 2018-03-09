-- Insert code to create Database Schema
-- This will create your .db database file for use

drop table if exists customers;
create table customers(
  customer_id integer primary key,
  company text not null,
  email text not null,
  fname text not null,
  lname text not null,
  phone text not null);

drop table if exists addressess;
create table addressess(
  id integer primary key,
  customer_id integer,
  street_address text not null,
  city text not null,
  state text not null,
  country text not null,
  zip_code integer not null);

drop table if exists orders;
create table orders(
  order_id integer primary key,
  part_name text not null,
  manufacturer text not null);

drop table if exists customers_orders;
create table customers_orders(
  id integer primary key,
  customer_id integer not null,
  order_id integer not null);

-- Dummy Data for testing

INSERT into customers (company, email, fname, lname, phone)
VALUES ("SPECTRE","hblofeld@spectre.net","Hans","Blofeld","510-393-8888");

INSERT into addressess (street_address, city, state, country, zip_code)
VALUES ("Unknown","Undisclosed","XX","Void","00000");

INSERT into orders (part_name, manufacturer)
VALUES ("fidget spinner", "Fidgies");
