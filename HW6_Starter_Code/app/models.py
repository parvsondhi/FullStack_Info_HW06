import sqlite3 as sql

# def insert_data():
#     # SQL statement to insert into database goes here
    
def insert_customer(first_name, last_name, company, email, phone_number):
    # SQL statement to insert into database
    with sql.connect('database.db') as con:
        cur = con.cursor() # creating cursor
        cur.execute("INSERT INTO customer (first_name, last_name, company, email, phone_number) VALUES (?,?,?,?,?)", (first_name, last_name, company, email, phone_number))
        con.commit() # commit = save to database
    return cur.lastrowid

def insert_address(street_address, city, state, country, zip_code, customer_id):
    with sql.connect('database.db') as con:
        cur = con.cursor() # creating cursor
        cur.execute("INSERT INTO address (street_address, city, state, country, zip_code, customer_id) VALUES (?,?,?,?,?,?)", (street_address, city, state, country, zip_code, customer_id))
        con.commit()

def retrieve_customers(): 
    # SQL statement to query database goes here
    with sql.connect('database.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor() # creating cursor
        result = cur.execute("select * from customer").fetchall() 
        print(result)
    return result

def insert_order (name_of_part, manufacturer_of_part):
    with sql.connect('database.db') as con:
        cur = con.cursor() 
        cur.execute("INSERT INTO 'orders' (name_of_part, manufacturer_of_part) VALUES (?,?)", (name_of_part, manufacturer_of_part))
        con.commit()
    return cur.lastrowid

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect('database.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor() # creating cursor
        result = cur.execute("SELECT orders.name_of_part, orders.manufacturer_of_part, customer_orders.customer_id FROM 'orders' INNER JOIN 'customer_orders' ON orders.order_id=customer_orders.order_id;").fetchall()
        print(result)
    return result

def insert_customer_orders(customer_id, order_id):
    with sql.connect('database.db') as con:
        cur = con.cursor() 
        cur.execute("INSERT INTO 'customer_orders' (customer_id, order_id) VALUES (?,?)", (customer_id, order_id))
        con.commit()


##You might have additional functions to access the database
