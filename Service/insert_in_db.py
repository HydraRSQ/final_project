from Service import update_project_info as info
import pymysql
from config import host, user, password, database



def employees_table(name, specialization, salary, bonus, project):
    """
    Adding an employee
    :param name:
    :param specialization:
    :param salary:
    :param bonus:
    :param project:
    :return:
    """
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    try:
        with connection:
            with connection.cursor() as cur:
                cur.execute(f'INSERT INTO `employees_table` (`id`, `name`, `specialization`, `salary`, `bonus`, `project`) VALUES (NULL, '
                            f'"{name}", "{specialization}", "{salary}", "{bonus}", "{project}")')
                connection.commit()
                cur.execute(f'Select id from projects_table where name = "{project}"')
                tmp = cur.fetchall()
                cur.execute(f'Select id from employees_table where name = "{name}" and project = "{project}"')
                user_id = cur.fetchall()[0][0]
                if len(tmp) != 0:
                    info.working_on_project(tmp[0][0])

                connection.commit()
        return {'id': user_id, 'success': True}
    except:
        return {'success':False}


def project_table(name, status,  budget, deadline):
    """
    Adding a project
    :param name:
    :param status:
    :param descript:
    :param budget:
    :param deadline:
    :return:
    """
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    try:
        with connection:
            with connection.cursor() as cur:
                cur.execute(f'INSERT INTO `projects_table` (`id`, `name`, `status`, `budget`, `deadline`, '
                            f'`employees`) VALUES (NULL, "{name}", "{status}", "{budget}", "{deadline}", "")')

                connection.commit()
                cur.execute(f'Select id from projects_table where name = "{name}"')
                tmp = cur.fetchall()
                connection.commit()
        return {'id': tmp, 'success': True}
    except Exception as err:
        return {'success':False, 'error' : err}