import pymysql
from config import host, user, password, database


def sort_employees(arr):
    """
    Returns data sorted by parameter
    :param arr:
    :return:
    """
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            if len(arr) == 0:
                data = 'Select * from employees_table'
            elif len(arr['search']) == 0:
                data = f'Select * from employees_table Order by "{arr["sort_type"]}"'
            else:
                data = f'Select * from employees_table Where name = "{arr["search"]}" or specialization = "{arr["search"]}" or salary = "{arr["search"]}" or bonus = "{arr["search"]}" ORDER by "{arr["sort_type"]}"'
            cur.execute(data)
            responce = cur.fetchall()
    return responce

def sort_projects(arr):
    """
    Returns data sorted by parameter
    :param arr:
    :return:
    """

    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            if len(arr) == 0:
                data = 'Select * from projects_table'
            elif len(arr['search']) == 0:
                data = f'Select * from projects_table Order by {arr["sort_type"]}'
            else:
                data = f'Select * from projects_table Where name = "{arr["search"]}" or status = "{arr["search"]}" or budget = "{arr["search"]}" or deadline = "{arr["search"]}" ORDER by "{arr["sort_type"]}"'

            cur.execute(data)
            responce = cur.fetchall()
    return responce


