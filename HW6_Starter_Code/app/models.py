import sqlite3 as sql

def insert_data():
    # SQL statement to insert into database goes here
    return

def insert_customer(first_name,last_name,company,email,phone):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as conn:
    	cur = conn.cursor()
    	cur.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, company, email, phone))
    	row = cur.execute('SELECT last_insert_rowid()').fetchone()[0]
    	conn.commit()
    return row

def insert_address(street_address,city,state,country,zipcode,customer):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as conn:
    	cur = conn.cursor()
    	cur.execute("INSERT INTO address (street_address, city, state, country, zip_code, customer_id) VALUES (?, ?, ?, ? , ?, ?)", (street_address, city, state, country, zipcode,customer))
    	conn.commit()

def insert_orders(name_of_part,manufacturer):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as conn:
    	cur = conn.cursor()
    	cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part) VALUES (?, ?)", (name_of_part, manufacturer))
    	row = cur.execute('SELECT last_insert_rowid()').fetchone()[0]
    	conn.commit()  
    return row

def insert_co(order_id,customer_id):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as conn:
    	cur = conn.cursor()
    	cur.execute("INSERT INTO customer_to_order (order_id, customer_id) VALUES (?, ?)", (order_id, customer_id))
    	conn.commit()  


def retrieve_customers():
    # SQL statement to query database goes here
	with sql.connect("app.db") as conn:
		conn.row_factory = sql.Row
		cur = conn.cursor()
		result = cur.execute("select * from customers").fetchall()
		print(result)
	return result

def retrieve_customer_to_orders():
    # SQL statement to query database goes here
	with sql.connect("app.db") as conn:
		conn.row_factory = sql.Row
		cur = conn.cursor()
		result = cur.execute("select * from customer_to_order, orders where orders.order_id = customer_to_order.order_id").fetchall()
		print(result)
	return result

##You might have additional functions to access the database
