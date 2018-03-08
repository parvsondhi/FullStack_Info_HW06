import sqlite3 as sql

#def insert_data():
    # SQL statement to insert into database goes here

def insert_customer(first_name, last_name, company, email, phone):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?,?,?,?,?)", (first_name, last_name, company, email, phone))
        con.commit()


def insert_address(street_address, city, state, country, zip_code):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO addresses (street_address, city, state, country, zip_code) VALUES (?,?,?,?,?)", (street_address, city, state, country, zip_code))
        con.commit()

def retrieve_customers():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from customers").fetchall()
        print(result)
    return result

def insert_order(name_of_part, manufacturer_of_part):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES (?,?)", (name_of_part, manufacturer_of_part))
        con.commit()

def retrieve_orders():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from orders").fetchall()
        print(result)
    return result