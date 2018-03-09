import sqlite3 as sql

def insert_data(firstName,lastName,company,email,phone):
    # SQL statement to insert into database goes here
    with sql.connect('database.db') as con:
    	cur = con.cursor()
    	cur.execute("INSERT INTO customer (firstName,lastName,company,email,phone) VALUES (?, ?, ?, ?, ?)", [firstName,lastName,company,email,phone])
    	con.commit()
    return cur.lastrowid


def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect('database.db') as con:
    	# create a cursor
    	con.row_factory = sql.Row
    	cur = con.cursor() 
    	result = cur.execute("SELECT * from customer").fetchall()
    return result


def retrieve_orders():
#     # SQL statement to query database goes here
	with sql.connect('database.db') as con:
    	# create a cursor
		con.row_factory = sql.Row
		cur = con.cursor() 
		result = cur.execute("SELECT * from order_to").fetchall()
	return result

# def retrive_customer_id():
# 	with sql.connect('database.db') as con:
#     	# create a cursor
# 		con.row_factory = sql.Row
# 		cur = con.cursor() 
# 		result = cur.execute("SELECT customer_id from order_to").fetchone()
# 	return result


def insert_order(partName, manufacturerName,customer_id):
    # SQL statement to insert into database goes here
    with sql.connect('database.db') as con:
    	cur = con.cursor()
    	cur.execute("INSERT INTO order_to (partName,manufacturerName,customer_id) VALUES (?, ?, ?)", [partName, manufacturerName,customer_id])
    	con.commit()
    return cur.lastrowid

def insert_cus_order(customer_id,order_id):
	with sql.connect('database.db') as con:
		cur = con.cursor()
		cur.execute("INSERT INTO cus_order (customer_id,order_id) VALUES (?, ?)", [customer_id, order_id])
		con.commit()


##You might have additional functions to access the database

# customer: (customer_id, first_name, last_name, company, email, phone) 
# address: (id, street_address, city, state, country, zip_code)