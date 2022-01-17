import pymysql
from config import host, user, password, database

connection = pymysql.connect(host=host, user=user, password=password, database=database)

def update_project(**kwargs):
    """
    Updating data in a table using specified keys
    :param kwargs:
    :return:
    """
    try:
        with connection:
            with connection.cursor() as cur:
                for key in kwargs:
                    if kwargs[key] == '':
                        continue
                    cur.execute(f'Update projects_table Set "{key}" = "{kwargs[key]}"where id = {kwargs["id"]}')
                    con.commit()
        return {'success': True}
    except:
        return {'success':False}


def update_employees(**kwargs):
    """
    Updating data in a table using specified keys
    :param kwargs:
    :return:
    """
    try:
        with connection:
            with connection.cursor() as cur:
                for key in kwargs:
                    if kwargs[key] == '':
                        continue
                    cur.execute(f'Update employees_table Set "{key}" = "{kwargs[key]}"where id = {kwargs["id"]}')
                    con.commit()
        return {'success': True}
    except:
        return {'success':False}