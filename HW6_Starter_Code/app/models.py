import sqlite3 as sql

## customers functions

def insert_customer(fname, lname, company, email, phone):
    # SQL statement to insert into database goes here
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	cur.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?,?,?,?,?)", (fname, lname, company, email, phone))
    	con.commit()
    	return cur.lastrowid

# def retrieve_customer(fname, lname):
#     # SQL statement to query database goes here
#     with sql.connect("database.db") as con:
#     	con.row_factory = sql.Row
#     	cur = con.cursor()
#     	result = cur.execute('select customer_id from customers where first_name = "' + fname + '" and last_name = "' + last_name + '"').fetchone() 
#     	return result


def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("database.db") as con:
    	con.row_factory = sql.Row
    	cur = con.cursor()
    	result = cur.execute("select * from customers").fetchall() # fetchone will retrieve the first result
    	return result


## address functions

def insert_address(street_address, city, state, country, zipcode, customer_id):
# def insert_address(street_address, city, state, country, zipcode):
    # SQL statement to insert into database goes here
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	cur.execute("INSERT INTO address (street_address, city, state, country, zipcode, customer_id) VALUES (?,?,?,?,?,?)", (street_address, city, state, country, zipcode, customer_id))
    	con.commit()

## orders functions

def insert_order(name_of_part, manufacturer_of_part, customer_id):
    # SQL statement to insert into database goes here
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?,?,?)", (name_of_part, manufacturer_of_part, customer_id))
    	con.commit()
    	return cur.lastrowid

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("database.db") as con:
    	con.row_factory = sql.Row
    	cur = con.cursor()
    	result = cur.execute("select * from orders").fetchall() # fetchone will retrieve the first result
    	return result

## customer_orders functions

def insert_customer_order(customer_id, order_id):
    # SQL statement to insert into database goes here
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	cur.execute("INSERT INTO customers_orders (customer_id, order_id) VALUES (?,?)", (customer_id, order_id))
    	con.commit()