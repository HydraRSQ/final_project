import pymysql
from config import host, user, password, database


def working_on_project(project_id):
    """
    Updates the number of employees on the project
    :param project_id:
    :return:
    """
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    try:
        with connection:
            with connection.cursor() as cur:
                cur.execute(f'Select name from projects_table where id = "{project_id}"')
                project_name = cur.fetchall()[0][0]
                cur.execute(f'Select id from employees_table where project = "{project_name}"')
                responce = cur.fetchall()
                data = len(responce)
                cur.execute(
                    f'UPDATE `projects_table` SET `employees` = "{data}" WHERE `projects_table`.`id` = "{project_id}"')
                connection.commit()
                return {'success': True}
    except:
        return {'success': False}


