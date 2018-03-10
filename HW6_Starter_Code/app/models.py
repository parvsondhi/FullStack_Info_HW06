import sqlite3 as sql

#def insert_data():
	# SQL statement to insert into database goes here
#	return null

def add_customer(first_name, last_name, company, email, phone):
	# SQL statement to insert into database goes here
	with sql.connect("database.db") as dbcon:
		c = dbcon.cursor()
		c.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, company, email, phone))
		#customer_id = c.execute("SELECT customer_id FROM customers WHERE first_name = ? AND last_name = ? AND company = ? AND email = ? AND phone = ?", (first_name, last_name, company, email, phone))
		dbcon.commit()
	return c.lastrowid

def add_address(street_address, city, state, country, zip_code, customer_id):
	# SQL statement to insert into database goes here
	with sql.connect("database.db") as dbcon:
		c = dbcon.cursor()
		c.execute("INSERT INTO addresses (street_address, city, state, country, zip_code, customer_id) VALUES (?, ?, ?, ?, ?, ?)", (street_address, city, state, country, zip_code, customer_id))
		dbcon.commit()

def add_order(name_of_part, manufacturer_of_part, customer_id):
	# SQL statement to insert into database goes here
	with sql.connect("database.db") as dbcon:
		c = dbcon.cursor()
		c.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?, ?, ?)", (name_of_part, manufacturer_of_part, customer_id))
		dbcon.commit()

def retrieve_customers():
	# SQL statement to query database goes here
	with sql.connect("database.db") as dbcon:
		c = dbcon.cursor()
		customer_data = c.execute("SELECT first_name, last_name, company, email, phone FROM customers").fetchall()
		#dbcon.commit()
		print(customer_data)
	return customer_data

def retrieve_orders():
	# SQL statement to query database goes here
	with sql.connect("database.db") as dbcon:
		c = dbcon.cursor()
		order_data = c.execute("SELECT customer_id, name_of_part, manufacturer_of_part FROM orders").fetchall()
		#dbcon.commit()
		print(order_data)
	return order_data

##You might have additional functions to access the database
