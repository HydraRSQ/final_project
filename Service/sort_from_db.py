import sqlite3


def sort_employees(arr):
    """
    Returns data sorted by parameter
    :param arr:
    :return:
    """
    if len(arr['search']) == 0:
        data = f'Select * from employees_table Order by "{arr["sort_type"]}"'
    else:
        data = f'Select * from employees_table Where name = "{arr["search"]}" or specialization = "{arr["search"]}" or salary = "{arr["search"]}" or bonus = "{arr["search"]}" ORDER by "{arr["sort_type"]}"'
    return data

def sort_projects(arr):
    """
    Returns data sorted by parameter
    :param arr:
    :return:
    """
    if len(arr['search']) == 0:
        data = f'Select * from projects_table Order by {arr["sort_type"]}'
    else:
        data = f'Select * from projects_table Where name = "{arr["search"]}" or status = "{arr["search"]}" or budget = "{arr["search"]}" or deadline = "{arr["search"]}" ORDER by "{arr["sort_type"]}"'
    return data
