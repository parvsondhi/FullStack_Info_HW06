import sqlite3 as sql

def insert_customer(first_name, last_name, company, email, phone):
    with sql.connect('database.db') as connection:
    	cursor = connection.cursor()
    	cursor.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?,?,?,?,?)",(first_name, last_name, company, email, phone))
    	connection.commit()


def insert_address(street_address, city, state, country, zip_code, customer_id):
	with sql.connect('database.db') as connection:
		cursor = connection.cursor()
		cursor.execute("INSERT INTO address (street_address, city, state, country, zip_code, customer_id) VALUES (?,?,?,?,?,?)", (street_address, city, state, country, zip_code, customer_id))
		connection.commit()

def insert_order(name_of_part, manufacturer_of_part, customer_id):
	with sql.connect('database.db') as connection:
		cursor = connection.cursor()
		cursor.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?,?,?)", (name_of_part, manufacturer_of_part, customer_id))
		connection.commit()

def insert_customer_order(customer_id, order_id):
	with sql.connect('database.db') as connection:
		cursor = connection.cursor()
		cursor.execute("INSERT INTO customer_order (customer_id, order_id) VALUES (?, ?)", (customer_id, order_id))
		connection.commit()

def retrieve_customers():
    with sql.connect('database.db') as connection:
    	connection.row_factory = sql.Row
    	cursor = connection.cursor()
    	result = cursor.execute("SELECT * FROM customers").fetchall()
    	return result

def retrieve_orders():
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		result = cursor.execute("SELECT * FROM orders").fetchall()
		return result

def retrieve_customer_id():
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		result = cursor.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1").fetchall()
		for row in result:
			return row[0]


def retrieve_order_id():
	with sql.connect('database.db') as connection:
		connection.row_factory = sql.Row
		cursor = connection.cursor()
		result = cursor.execute("SELECT * FROM orders ORDER BY order_id DESC LIMIT 1").fetchall()
		for row in result:
			return row[0]
