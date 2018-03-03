-- Insert code to create Database Schema
-- This will create your .db database file for use

DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
    `customer_id`           INT      PRIMARY KEY, 
    `first_name`            TEXT     NOT NULL, 
    `last_name`             TEXT     NOT NULL, 
    `company`               TEXT, 
    `email`                 TEXT, 
    `phone`                 TEXT
);

DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
    `id`                    INT     PRIMARY KEY, 
    `customer_id`           INT     NOT NULL,
    `street_address`        TEXT    NOT NULL, 
    `city`                  TEXT    NOT NULL, 
    `zip_code`              TEXT    NOT NULL,
    `state`                 TEXT, 
    `country`               TEXT, 

    FOREIGN KEY (`customer_id`) REFERENCES `customer`(`customer_id`) ON DELETE CASCADE
);

DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
    `order_id`              INT     PRIMARY KEY, 
    `name_of_part`          TEXT    NOT NULL,
    `manufacturer_of_part`  TEXT    NOT NULL
);

DROP TABLE IF EXISTS `customer_order`;
CREATE TABLE `customer_order` (
    `id`                    INT     PRIMARY KEY,
    `order_id`              INT     NOT NULL, 
    `customer_id`           INT     NOT NULL,

    FOREIGN KEY (`order_id`) REFERENCES `order`(`order_id`) ON DELETE CASCADE,
    FOREIGN KEY (`customer_id`) REFERENCES `customer`(`customer_id`) ON DELETE CASCADE
);

