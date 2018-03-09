import sqlite3 as sql

DB_PATH = 'app.db'

def get_last_row_id(con):
    return con.execute('SELECT last_insert_rowid()').fetchone()[0]


# ================
# Addresses
# ================

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


def get_addresses_for_customer_id(customer_id):
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute(
            '''
                SELECT *
                FROM `address`
                WHERE `customer_id` = ?
                ORDER BY `id` DESC;
            '''
        , [str(customer_id)])
        
        return list(map(lambda row: address_row_to_object(row), cursor.fetchall()))

    return []

def retrieve_one_addresss_by_id(id):
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute('''
            SELECT * 
            FROM `address`
            WHERE `id`=?;
        ''',
        (id))

        record = cursor.fetchone()
        if (record is not None):
            return address_row_to_object(record)
        else:
            return None

    return None
    

def insert_address_for_customer(customer_id, form):
    query = '''
        INSERT INTO `address` (`customer_id`, `street_address`, `city`, `zip_code`, `state`, `country`)  
        VALUES (?,?,?,?,?,?);
    '''
    with sql.connect(DB_PATH) as con: 
        con.execute(query, [customer_id, form.street_address.data, form.city.data, form.zip_code.data, form.state.data, form.country.data])
        con.commit()
    
def update_address(address_id, form):
    query = '''
        UPDATE `address` 
        SET `street_address`=?, `city`=?, `zip_code`=?, `state`=?, `country`=?
        WHERE `id`=?;
    '''

    with sql.connect(DB_PATH) as con: 
        con.execute(query, [form.street_address.data, form.city.data, form.zip_code.data, form.state.data, form.country.data, address_id])
        con.commit()


# ================
# CUSTOMERS
# ================

def customer_row_to_object(row):

    addresses = get_addresses_for_customer_id(row[0])

    return {
        'customer_id': row[0],
        'first_name': row[1],
        'last_name': row[2],
        'company': row[3],
        'email': row[4],
        'phone': row[5],
        'addresses': addresses
    }

def insert_customer(form):
    query = '''
        INSERT INTO `customer` (`first_name`, `last_name`, `company`, `email`, `phone`)  
        VALUES (?,?,?,?,?);
    '''
    with sql.connect(DB_PATH) as con: 
        con.execute(query, [form.first_name.data, form.last_name.data, form.company.data, form.email.data, form.phone.data])
        con.commit()
    
        return get_last_row_id(con)

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute('''
            SELECT * 
            FROM `customer`;
        ''')
        
        return list(map(lambda row: customer_row_to_object(row), cursor.fetchall()))

    return []

def retrieve_customers_by_ids(ids):
    if (len(ids) == 0):
        return []

    query = '''
            SELECT * 
            FROM `customer`
            WHERE `customer_id` in ({});
            '''
    query = query.format(', '.join(['?']*len(ids)))

    with sql.connect(DB_PATH) as con: 
        cursor = con.execute(query, ids)

        return list(map(lambda row: customer_row_to_object(row), cursor.fetchall()))

    return []

def retrieve_one_customer_by_id(id):
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute('''
            SELECT * 
            FROM `customer`
            WHERE `customer_id`=?;
        ''',
        (id))

        record = cursor.fetchone()
        if (record is not None):
            return customer_row_to_object(record)
        else:
            return None

    return None

def update_customer(customer_id, form):
    query = '''
        UPDATE `customer` 
        SET `first_name`=?, `last_name`=?, `company`=?, `email`=?, `phone`=?
        WHERE `customer_id`=?;
    '''

    with sql.connect(DB_PATH) as con: 
        con.execute(query, [form.first_name.data, form.last_name.data, form.company.data, form.email.data, form.phone.data, customer_id])
        con.commit()


# ================
# ORDERS
# ================

def order_row_to_object(row):
    # Note: I am aware that this doesn't scale at all, but wrt
    # the scope of this exercise, I don't mind for now.

    customers = get_customers_for_order_id(row[0])

    return {
        'order_id': row[0],
        'name_of_part': row[1],
        'manufacturer_of_part': row[2],
        'customers': customers
    }

def get_customers_for_order_id(order_id):
    customer_ids = []
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute(
            '''
                SELECT `customer_id`
                FROM `customer_order`
                WHERE `order_id` = ?;
            '''
        , [str(order_id)])
        
        customer_ids = [r[0] for r in cursor.fetchall()]

    return retrieve_customers_by_ids(customer_ids)


def retrieve_orders():
    # SQL statement to query database goes here
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute('''
            SELECT * 
            FROM `order`;
        ''');
        
        return list(map(lambda row: order_row_to_object(row), cursor.fetchall()))

    return []


def retrieve_one_order_by_id(id):
    # SQL statement to query database goes here
    with sql.connect(DB_PATH) as con: 
        cursor = con.execute('''
            SELECT * 
            FROM `order`
            WHERE `order_id`=?;
        ''', [id])

        record = cursor.fetchone()
        if (record is not None):
            return order_row_to_object(record)
        else:
            return None

    return None


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

        return order_id
        
    return None

def update_order(order_id, form):
    query = '''
        UPDATE `order` 
        SET `name_of_part`=? , `manufacturer_of_part`=?
        WHERE `order_id`=?;
    '''

    with sql.connect(DB_PATH) as con: 
        con.execute(query, [form.name_of_part.data, form.manufacturer_of_part.data, order_id])
        con.commit()
