import sys
sys.path.append('../')
from main import app
from Service import insert_in_db as insert
from Service import sort_from_db as sort_by_db
from Service import delete_from_db as delete
from Service import select_from_db as select
from Service import update_project_info as update_project
from Service import update_table as update
from Service import create_base
import pymysql
from config import host, user, password, database



def test_main_page():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_projects_page():
    response = app.test_client().get('/projects')

    assert response.status_code == 200


def test_create_employee_page():
    response = app.test_client().get('/create_employee')

    assert response.status_code == 200


def test_create_project_page():
    response = app.test_client().get('/create_project')

    assert response.status_code == 200


def test_employees_page():
    response = app.test_client().get('/employees')

    assert response.status_code == 200





def test_delete_project():
    response = app.test_client().get('/delete_project')
    assert response.status_code == 302


def test_create_new_project():
    assert insert.project_table('Test', 'run', 10000, '12-11-2022')['success'] == True


def test_project_info_page():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select id from projects_table where name = "Test"')
            proj_id = cur.fetchall()[0][0]
            response = app.test_client().get(f'/project_info/{proj_id}')

    assert response.status_code == 200

def test_project_info_api():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select id from projects_table where name = "Test"')
            proj_id = cur.fetchall()[0][0]
            response = app.test_client().get(f'/api/v1.0/info_project/{proj_id}')
    assert response.status_code == 200


def test_update_project_info():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select id from projects_table where name = "Test"')
            proj_id = cur.fetchall()[0][0]
    assert update_project.working_on_project(proj_id)['success'] == True

def test_delete_project_func():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select id from projects_table where name = "Test"')
            proj_id = cur.fetchall()[0][0]
    assert delete.delete_project(proj_id)['success'] == True


def test_create_new_employee():
    assert insert.employees_table('Test_employee', 123, 12000, 511, 'Test_proj')['success'] == True


def test_employee_profile_page():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select id from employees_table where name = "Test_employee"')
            proj_id = cur.fetchall()[0][0]

    response = app.test_client().get(f'/profile_employee/{proj_id}')

    assert response.status_code == 200


def test_employee_profile_api():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select id from employees_table where name = "Test_employee"')
            proj_id = cur.fetchall()[0][0]
    response = app.test_client().get(f'/api/v1.0/info_employee/{proj_id}')
    assert response.status_code == 200



def test_delete_employee_func():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select id from employees_table where name = "Test_employee"')
            proj_id = cur.fetchall()[0][0]
    assert delete.delete_project(proj_id)['success'] == True


def test_create_base():
    assert create_base.create_tables()['success'] == True
