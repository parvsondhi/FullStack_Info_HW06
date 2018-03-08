import sqlite3 as sql

def insert_customer(first_name, last_name, company, email, phone):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("INSERT INTO customer (first_name, last_name, company, email, phone) VALUES (?, ?, ?, ?, ?)", (first_name,last_name,company,email,phone))
		con.commit()

def insert_address(street_address, city, state, country, zip_code):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		result = cur.execute("SELECT * FROM customer ORDER BY customer_id DESC LIMIT 1").fetchall()
		for row in result:
			foreign_id = row[0]
		cur.execute("INSERT INTO address (street_address, city, state, country, zip_code, customer_id) VALUES (?, ?, ?, ?, ?, ?)", (street_address,city,state,country,zip_code, foreign_id))
		con.commit()

def insert_order(name_of_part, manufacturer_of_part, foreign_id):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?, ?, ?)", (name_of_part,manufacturer_of_part,foreign_id))
		con.commit()

def retrieve_customers():
    # DONE NSQL statement to query database goes here
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        retrieved_customers = cur.execute("select * from customer").fetchall()
        
        # for row in retrieved_customers:
        # 	return row[0]
        print (retrieved_customers)
    return retrieved_customers

def retrieve_addresses():
    # DONE NSQL statement to query database goes here
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        retrieved_addresses = cur.execute("select * from address").fetchall()
        print (retrieved_addresses)
    return retrieved_addresses

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        retrieved_orders = cur.execute("select * from orders").fetchall()
        print (retrieved_orders)
    return retrieved_orders

##You might have additional functions to access the database

# EXAMPLES FROM LAB08
# def insert_customer(company,email):
#     with sql.connect("app.db") as con:
#         cur = con.cursor()
#         cur.execute("INSERT INTO customers (company,email) VALUES (?,?)", (company,email))
#         con.commit()

# def retrieve_customers():
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         result = cur.execute("select * from customers").fetchall()
#         print (result)
#     return result