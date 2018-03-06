
import sqlite3 as sql

def insert_customer(customer, address):
    # SQL statement to insert into database goes here
    with sql.connect('app.db') as db:
        cursor = db.cursor()
        cursor.execute('''INSERT INTO customer(first_name, last_name, company, email, phone)
                      VALUES(?,?,?,?,?)''', customer)
        cursor.execute('''INSERT INTO address(street_address, city, state, country, zip_code, customer_id)
                      VALUES(?,?,?,?,?,(SELECT MAX(customer_id) FROM customer))''', address)
        db.commit()

def insert_order(order, customer_id):
    with sql.connect('app.db') as db:
        cursor = db.cursor()
        cursor.execute('''INSERT INTO orders(name_of_part, manufacturer_of_part)
                      VALUES(?,?)''', order)
        cursor.execute('''INSERT INTO customer_orders(order_id, customer_id)
                      VALUES((SELECT MAX(order_id) FROM orders),?)''', customer_id)
        db.commit()

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect('app.db') as db:
        db.row_factory = sql.Row
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM customer''')
        return cursor.fetchall()

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect('app.db') as db:
        db.row_factory = sql.Row
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM orders join customer_orders on orders.order_id = customer_orders.order_id''')
        return cursor.fetchall()

##You might have additional functions to access the database
