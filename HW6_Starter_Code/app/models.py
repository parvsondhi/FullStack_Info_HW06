import sqlite3 as sql

# Add a customer to the database
def insert_customer(firstName, lastName, company, email, telephone):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?,?,?,?,?)", (firstName, lastName, company, email, telephone))
        # Added this
        lastID = cur.execute("SELECT last_insert_rowid() AS last_id").fetchone()
        con.commit()
        # Added this
        return lastID

# This returns all customers 
def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM customers").fetchall()
        # print(result)
        return result

# This function is not needed anymore
def retrieve_customer_id(firstName, lastName):
	with sql.connect("app.db") as con:
		con.row_factory = sql.Row
		cur = con.cursor()
		query = "SELECT customer_id FROM customers WHERE first_name == '%s' and last_name == '%s'" % (firstName, lastName)
		result = cur.execute( query ).fetchone()
		# print(result)
		return result

# This is used to pass the id to the address as the email is a unique attribute
def retrieve_customer_id_byemail(value):
	with sql.connect("app.db") as con:
		con.row_factory = sql.Row
		cur = con.cursor()
		query = "SELECT customer_id FROM customers WHERE email == '%s'" % (value)
		result = cur.execute( query ).fetchone()
		# print(result)
		return result


def insert_order(nameOfPart, manufacturerOfPart):
	# SQL statement to insert into database goes here
	with sql.connect("app.db") as con:
		cur = con.cursor()
		cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part) VALUES (?,?)", (nameOfPart, manufacturerOfPart))
		lastID = cur.execute("SELECT last_insert_rowid() AS last_id").fetchone()
		con.commit()
		return lastID

# Insert order and customer id into the matching database
def insert_order_match(orderID, customerID):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO order_match (order_id, customer_id) VALUES (?,?)", (orderID, customerID))
        con.commit()

#  Return all orders
def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT * FROM orders").fetchall()
        # print(result)
        return result

# GEt customer ID of an order based on order id
def retrieve_order_match(oID):
	with sql.connect("app.db") as con:
		con.row_factory = sql.Row
		cur = con.cursor()
		query = "SELECT customer_id FROM order_match WHERE order_id == '%s'" % (oID)
		result = cur.execute( query ).fetchone()
		# print(result)
		return result

# Insert address into the database
def insert_address(addressID, streetAddress, state, country, zipCode):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO addresses (id, street_address, state_, country, zip_code) VALUES (?,?,?,?,?)", (addressID, streetAddress, state, country, zipCode))
        con.commit()
