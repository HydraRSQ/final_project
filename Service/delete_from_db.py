import sqlite3
import json

def delete_employee(id):
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    dat = cur.execute(f'Select 1 from employees_table where id = "{id}"').fetchall()
    cur.execute(f'delete from employees_table where id = "{id}"')
    con.commit()
    if len(dat) == 0:
        result = {'result': False}
    else:
        result = {'result': True}
    return json.dumps(result)

def delete_project(id):
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    dat = cur.execute(f'Select 1 from projects_table where id = "{id}"').fetchall()
    cur.execute(f'delete from projects_table where id = "{id}"')
    con.commit()
    if len(dat) == 0:
        result = {'result': False}
    else:
        result = {'result': True}
    return json.dumps(result)

