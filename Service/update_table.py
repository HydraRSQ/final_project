import sqlite3


def update_project(**kwargs):
    """
    Updating data in a table using specified keys
    :param kwargs:
    :return:
    """
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    for key in kwargs:
        if kwargs[key] == '':
            continue
        cur.execute(f'Update projects_table Set "{key}" = "{kwargs[key]}"where id = {kwargs["id"]}')
        con.commit()
    return


def update_employees(**kwargs):
    """
    Updating data in a table using specified keys
    :param kwargs:
    :return:
    """
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    for key in kwargs:
        if kwargs[key] == '':
            continue
        cur.execute(f'Update employees_table Set "{key}" = "{kwargs[key]}"where id = {kwargs["id"]}')
        con.commit()
    return