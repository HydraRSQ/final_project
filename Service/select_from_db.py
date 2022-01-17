import pymysql
from config import host, user, password, database

connection = pymysql.connect(host=host, user=user, password=password, database=database)

def select_project(id):
    """
    Getting data from database to json by id
    :param id:
    :return:
    """
    with connection:
        with connection.cursor() as cur:
            cur.execute(f'Select * from projects_table where id = {id}')
            tmp = cur.fetchall()
            data = {}
            cur.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = "projects_table"')
            all_calumn = cur.fetchall()
            x = 0
            for i in all_calumn:
                data[i[0]] = tmp[0][x]
                x += 1
    return data


def select_employees(id):
    """
    Getting data from database to json by id
    :param id:
    :return:
    """
    with connection:
        with connection.cursor() as cur:
            cur.execute(f'Select * from employees_table where id = {id}')
            tmp = cur.fetchall()
            data = {}
            cur.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = "employees_table"')
            all_calumn = cur.fetchall()
            x = 0
            for i in all_calumn:
                data[i[0]] = tmp[0][x]
                x += 1
    return data


