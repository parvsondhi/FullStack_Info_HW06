import sqlite3 as sql

DB_PATH = 'app.db'

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


def insert_data():
    # SQL statement to insert into database goes here
    return

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

def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute('''
            SELECT * 
            FROM `order`;
        ''');
        
        return cursor.fetchall()

    return []


##You might have additional functions to access the database
