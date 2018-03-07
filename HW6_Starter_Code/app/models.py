import sqlite3 as sql

DB_PATH = 'app.db'

def get_last_row_id(con):
    return con.execute('SELECT last_insert_rowid()').fetchone()[0]

# ================
# CUSTOMERS
# ================

def customer_row_to_object(row):
    return {
        'customer_id': row[0],
        'first_name': row[1],
        'last_name': row[2],
        'company': row[3],
        'email': row[4],
        'phone': row[5],
    }

def address_row_to_object(row):
    return {
        'id': row[0],
        'customer_id': row[1],
        'street_address': row[2],
        'city': row[3],
        'zip_code': row[4],
        'state': row[5],
        'country': row[6],
    }

def insert_customer(form):
    query = '''
        INSERT INTO `customer` (`first_name`, `last_name`, `company`, `email`, `phone`)  
        VALUES (?,?,?,?,?);
    '''
    with sql.connect(DB_PATH) as con: 
        con.execute(query, [form.first_name.data, form.last_name.data, form.company.data, form.email.data, form.phone.data])
        con.commit()
    

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute('''
            SELECT * 
            FROM `customer`;
        ''');

        # print(list(map(lambda row: customer_row_to_object(row), cursor.fetchall())))
        
        return list(map(lambda row: customer_row_to_object(row), cursor.fetchall()))

    return []

def retrieve_customer(id):
    # SQL statement to query database goes here
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute('''
            SELECT * 
            FROM `customer`
            WHERE `customer_id`=?;
        ''',
        (id));

        record = cursor.fetchone()
        if (record is not None):
            return customer_row_to_object(record)
        else:
            return None

    return None

# ================
# ORDERS
# ================

def order_row_to_object(row):
    return {
        'order_id': row[0],
        'name_of_part': row[1],
        'manufacturer_of_part': row[2]
    }

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute('''
            SELECT * 
            FROM `order`;
        ''');
        
        return list(map(lambda row: order_row_to_object(row), cursor.fetchall()))

    return []

def insert_order(customer_id, form):
    query_1 = '''
        INSERT INTO `order` (`name_of_part`, `manufacturer_of_part`)  
        VALUES (?,?);
    '''
    query_2 = '''
        INSERT INTO `customer_order` (`customer_id`, `order_id`)  
        VALUES (?,?);
    '''

    with sql.connect(DB_PATH) as con: 
        con.execute(query_1, [form.name_of_part.data, form.manufacturer_of_part.data])
        con.commit()

        order_id = get_last_row_id(con)

        con.execute(query_2, [customer_id, order_id])
        
##You might have additional functions to access the database
