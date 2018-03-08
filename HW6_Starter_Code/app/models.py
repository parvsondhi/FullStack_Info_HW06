import sqlite3 as sql

def insert_customerData(company_name,email_id, first, last, phone):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()			#access the the database you just connected to
#primary key is automatically added by normal incrementation. If you want otherwise, u need to manually add it
        cur.execute("INSERT into customers (company, email, first_name, last_name, phone) VALUES (?, ?, ?, ?, ?)"
    	   , (company_name, email_id, first, last, phone))
        con.commit()
        return cur.lastrowid  #returning the last auto incremented value which is the customer id for us
 
def insert_addressData(street, city, state, country, zipp, frgnID):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()			#access the the database you just connected to
#primary key is automatically added by normal incrementation. If you want otherwise, u need to manually add it
        cur.execute("INSERT into address (street_address, city, state, country, zip_code, customer_id) VALUES (?, ?, ?, ?, ?, ?)"
    	   , (street, city, state, country, zipp, frgnID))
        con.commit()

def insert_orderData(part, manufacturer, frgnID):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()			#access the the database you just connected to
#primary key is automatically added by normal incrementation. If you want otherwise, u need to manually add it
        cur.execute("INSERT into orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?, ?, ?)"
            , (part, manufacturer, frgnID))
        con.commit()
        return cur.lastrowid
    
def insert_customerOrderData(customer_id, order_id):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()          #access the the database you just connected to
#primary key is automatically added by normal incrementation. If you want otherwise, u need to manually add it
        cur.execute("INSERT into customersOrders (customer_id, order_id) VALUES (?, ?)"
            , ( customer_id, order_id))
        con.commit()


def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row 		#Ensuring u r receiving data as actual row objects
        cur = con.cursor()
        result = cur.execute("SELECT * FROM customers").fetchall()   #another option is fetchone()
																	 # which returns the first row from the db
        return result

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row 		#Ensuring u r receiving data as actual row objects
        cur = con.cursor()
        result = cur.execute("SELECT * FROM orders").fetchall()   #another option is fetchone()
																	 # which returns the first row from the db
        return result

