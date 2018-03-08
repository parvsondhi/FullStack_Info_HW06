import sqlite3 as sql

def insert_customer(first_name, last_name, company, email, phone, street, city, state, country, zip_code):
    # SQL statement to insert into database goes here
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?,?,?,?,?)", (first_name, last_name, company, email, phone))
        cur.execute("INSERT INTO address (street, city, state, country, zip_code, customer_id) VALUES (?,?,?,?,?,?)", (street, city, state, country, zip_code, cur.lastrowid))
        con.commit()

def insert_order(value, name_of_part, manufacturer_of_part):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part) VALUES (?,?)", (name_of_part, manufacturer_of_part))
        cur.execute("INSERT INTO customers_orders (customer_id, order_id ) VALUES (?,?)", (value, cur.lastrowid))
        con.commit()

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("database.db") as con:
        # establish the connection 
        con.row_factory = sql.Row
        cur = con.cursor()
        # fetch all will fetch all lol. there is fetch one too.
        result = cur.execute("select * from customers").fetchall()
        print (result)
    return result

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("database.db") as con:
        # establish the connection 
        con.row_factory = sql.Row
        cur = con.cursor()
        # fetch all will fetch all lol. there is fetch one too.
        # result = cur.execute("SELECT * FROM orders INNER JOIN ").fetchall()
        result = cur.execute("SELECT orders.order_id, orders.name_of_part, orders.manufacturer_of_part,  customers_orders.customer_id from orders INNER JOIN customers_orders ON orders.order_id = customers_orders.order_id").fetchall()
        print (result)
    return result


##You might have additional functions to access the database