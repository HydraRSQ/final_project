import pymysql
from config import host, user, password, database



def delete_employee(id):
    """
    Removing an employee
    :param id:
    :return:
    """
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    try:
        with connection:
            with connection.cursor() as cur:
                cur.execute(f'delete from employees_table where id = "{id}"')
                connection.commit()
        return {'success': True}
    except:
        return {'success': False}


def delete_project(id):
    """
    Deleting a project
    :param id:
    :return:
    """
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    try:
        with connection:
            with connection.cursor() as cur:
                cur.execute(f'delete from projects_table where id = "{id}"')
                connection.commit()
        return {'success': True}

    except:
        return {'success': False}
