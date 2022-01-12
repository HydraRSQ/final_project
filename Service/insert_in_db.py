import sqlite3
from Service import update_project_info as info


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
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE if not exists employees_table (id	INTEGER PRIMARY KEY AUTOINCREMENT, name	TEXT, '
                'specialization	TEXT, salary	INTEGER, bonus	INTEGER, project	TEXT)')

    cur.execute(f'insert into employees_table (name, specialization, salary, bonus, project) values ("{name}", '
                f'"{specialization}", "{salary}","{bonus}","{project}")')
    tmp = cur.execute(f'Select id from projects_table where name = "{project}"').fetchall()
    con.commit()
    if len(tmp) != 0:
        info.working_on_project(tmp[0][0])
    return


def project_table(name, status, descript, budget, deadline):
    """
    Adding a project
    :param name:
    :param status:
    :param descript:
    :param budget:
    :param deadline:
    :return:
    """
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE if not exists projects_table (id	INTEGER PRIMARY KEY AUTOINCREMENT, name	TEXT, '
                'status	TEXT, descript	text, budget	INTEGER, deadline	TEXT, employees INTEGER)')

    cur.execute(
        f'insert into projects_table (name, status, descript, budget, deadline, employees) values ("{name}", '
        f'"{status}", "{descript}","{budget}","{deadline}", 0)')
    con.commit()
    return