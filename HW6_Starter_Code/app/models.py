import sqlite3 as sql

def insert_customer(company,email,first_name,last_name,phone):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
	    cur = con.cursor()
	    cur.execute("INSERT INTO customer (company,email,first_name,last_name,phone) VALUES (?,?,?,?,?)", (company,email,first_name,last_name,phone))
	    con.commit()

def insert_address(street_address,city,state,country,zip_code):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
	    cur = con.cursor()
	    cur.execute("INSERT INTO address (street_address,city,state,country,zip_code) VALUES (?,?,?,?,?)", (street_address,city,state,country,zip_code))
	    con.commit()

def insert_order(name_of_part, manufacturer_of_part):
    with sql.connect("app.db") as con:
	    cur = con.cursor()
	    cur.execute("INSERT INTO `order` (name_of_part, manufacturer_of_part) VALUES (?,?)", (name_of_part, manufacturer_of_part))
	    con.commit()

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from customer").fetchall()
        print(result)
    return result

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from `order`").fetchall()
        print(result)
    return result


##You might have additional functions to access the database
