import sqlite3 as sql

def retrieve_customers():
    conn = sql.connect('app.db')
    c = conn.cursor()
    results = []
    c.execute("SELECT * FROM customer")
    for row in c.execute('SELECT * FROM customer'): 
        customer = {}
        customer["company"] = row[3]
        customer["email"] = row[4]
        results.append(customer)
    conn.close()
    return results
def retrieve_orders():
    conn = sql.connect('app.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM purchase_order'): 
        print(row)
    conn.close()
    pass
def insert_customer (customer_id, first_name, last_name, company, email, phone): 
    conn = sql.connect('app.db')

    c = conn.cursor()
    c.execute("INSERT INTO customer VALUES (%d, '%s', '%s', '%s', '%s', '%s')" %(customer_id, first_name, last_name, company, email, phone))
    conn.commit()
    conn.close()
def insert_order (order_id, name_of_part, manufacturer_of_part): 
    conn = sql.connect('app.db')

    c = conn.cursor()
    c.execute("INSERT INTO purchase_order VALUES (%d, '%s', '%s')" %(order_id, name_of_part, manufacturer_of_part))
    conn.commit()
    conn.close()
def insert_customer_order (id, order_id, customer_id): 
    conn = sql.connect('app.db')

    c = conn.cursor()
    c.execute("INSERT INTO customer_order VALUES (%d, %d, %d)" %(id, order_id, customer_id))
    conn.commit()
    conn.close()
def insert_address (id, street_address, city, state, country, zip_code, customer_id): 
    conn = sql.connect('app.db')

    c = conn.cursor()
    c.execute("INSERT INTO address VALUES (%d, '%s', '%s', '%s', '%s', '%s',%d)" %(id, street_address, city, state, country, zip_code, customer_id))
    conn.commit()
    conn.close()

# insert_customer(12313,'br','rb','asf','asdfsa','123123')
# retrieve_customers()
# insert_order(12313,'br','rb')
# retrieve_orders()

