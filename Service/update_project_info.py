import sqlite3
import json


def working_on_project(project_id):
    con = sqlite3.connect('D:\Homework\project\Service\\base.db')
    cur = con.cursor()
    project_name = cur.execute(f'Select name from projects_table where id = "{project_id}"').fetchall()[0][0]
    data = len(cur.execute(f'Select id from employees_table where project = "{project_name}"').fetchall())
    cur.execute(f'Update projects_table set employees = "{data}" where name = "{project_name}"')
    con.commit()
    return
