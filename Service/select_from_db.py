import sqlite3
import json


def select_project(id):
    con = sqlite3.connect('D:\Homework\project\Service\\base.db')
    cur = con.cursor()
    tmp = cur.execute(f'Select * from projects_table where id = {id}').fetchall()[0]
    data = {}
    all_calumn = cur.execute('PRAGMA table_info(projects_table)').fetchall()
    con.commit()
    x = 0
    for i in all_calumn:
        data[i[1]] = tmp[x]
        x += 1
    json.dumps(data)
    return data


def select_employees(id):
    con = sqlite3.connect('D:\Homework\project\Service\\base.db')
    cur = con.cursor()
    tmp = cur.execute(f'Select * from employees_table where id = {id}').fetchall()[0]
    data = {}
    all_calumn = cur.execute('PRAGMA table_info(employees_table)').fetchall()
    con.commit()
    x = 0
    for i in all_calumn:
        data[i[1]] = tmp[x]
        x += 1
    json.dumps(data)
    return data
