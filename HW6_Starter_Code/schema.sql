-- Insert code to create Database Schema
-- This will create your .db database file for use

DROP TABLE if EXISTS customers;

CREATE TABLE customers (
  customer_id integer primary key,
  first_name text not null,
  last_name text not null,
  company text not null,
  email text not null,
  phone_number text not null
);

CREATE TABLE addresses (
  address_id integer primary key,
  street_address text not null,
  city text not null,
  state text not null,
  country text not null,
  zipcode integer not null,
  customer_id integer not null,
  FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE orders (
  order_id integer primary key,
  name_of_part text not null,
  manufacturer_of_part text not null,
  customer_id integer not null,
  FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE customer_order (
  id integer primary key,
  order_id integer not null,
  customer_id integer not  null,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
