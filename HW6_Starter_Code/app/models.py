import sqlite3 as sql

def insert_data(table, data):
    print('inserting to ' + table)
    with sql.connect("app.db") as con:
        nvars = len(data.keys())
        print(nvars)
        for i in range(1, nvars):
            if i==1: qs = '?'
            qs = qs + ', ?'
        print(qs)
        print(len(qs))
        keys = tuple(data.keys())
        print(keys)
        print(len(keys))
        vals = tuple(data.values())
        print(vals)
        print(len(vals))
        sql_string = f'INSERT INTO {table}{keys} VALUES({qs})'
        print(sql_string)
        cur = con.cursor()
        cur.execute(sql_string, vals)
        con.commit()
    return cur.lastrowid

def retrieve_data(table):
    print('retreiving from ' + table)
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        sql_string = f'SELECT * FROM {table}'
        result = cur.execute(sql_string).fetchall()
        print(result)
    return result
