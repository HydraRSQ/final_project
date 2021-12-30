from flask import Flask, render_template, request, redirect, make_response, jsonify, abort
import sqlite3
from Service import insert_in_db as insert
from Service import sort_from_db as sort_by_db
from Service import delete_from_db as delete
from Service import select_from_db as select
from Service import update_project_info as update_project
from Service import update_table as update
from graph import create_graph as create_graph
from flask import Markup
from loguru import logger

logger.add("debug.log", format="{time} {level} {message}", level= "DEBUG")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/statistics', methods=["POST", "GET"])
def test():
    fig = create_graph.project_graph()
    if request.method == 'POST':
        if 'salary' in request.form.keys():
            fig = create_graph.salary_graph()
        elif 'bonus' in request.form.keys():
            fig = create_graph.bonus_graph()
        elif 'projects' in request.form.keys():
            fig = create_graph.project_graph()
    logger.info(f"Show table")
    return render_template('statistics.html', div_placeholder=Markup(fig))


@app.route('/project_info/<user_id>', methods=["POST", "GET"])
def project_info(user_id):
    if request.method == 'POST':
        update_project.working_on_project(user_id)
        data = select.select_project(user_id)
        logger.info(f"Show project. ID: {user_id}")
        return render_template('project_info.html', data=data)

    logger.info(f"Wrong project id. ID: {user_id}")
    return render_template('not_found.html')


@app.route('/change_project', methods=["POST", "GET"])
def change_project():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        status = request.form['status']
        descript = request.form['descript']
        budget = request.form['budget']
        deadline = request.form['deadline']
        update.update_project(name=name, status=status, descript=descript, budget=budget, deadline=deadline,
                              id=id)

        logger.info(f"Change project. ID: {id}")

    return redirect('/projects')


@app.route('/projects', methods=["POST", "GET"])
def projects():
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    data = cur.execute('Select * from projects_table').fetchall()
    if request.method == "POST":
        data = cur.execute(sort_by_db.sort_projects(request.form)).fetchall()
    logger.info(f"Show projects")

    return render_template('projects.html', data=data)


@app.route('/delete_project', methods=["POST", "GET"])
def delete_project():
    if request.method == "POST":
        if 'delete' in request.form.keys():
            delete.delete_project(request.form['delete'])
    logger.info(f"Delete project")

    return redirect('/projects')


@app.route('/create_project', methods=["POST", "GET"])
def create_project():
    if request.method == "POST":
        name = request.form['name']
        status = request.form['status']
        descript = request.form['descript']
        budget = request.form['budget']
        deadline = request.form['deadline']
        insert.project_table(name, status, descript, budget, deadline)

        logger.info(f"Create project. Name: {name}")
        return redirect('/projects')

    return render_template('create_project.html')


@app.route('/employees', methods=["POST", "GET"])
def employees():
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    data = cur.execute('Select * from employees_table').fetchall()
    if request.method == "POST":
        data = cur.execute(sort_by_db.sort_employees(request.form)).fetchall()
    logger.info(f'Show employees')
    return render_template('employees.html', data=data)


@app.route('/change_employee', methods=["POST", "GET"])
def change_employee():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        salary = request.form['salary']
        bonus = request.form['bonus']
        project = request.form['project']
        specialization = request.form['specialization']
        update.update_employees(name=name, salary=salary, bonus=bonus, project=project, specialization=specialization,
                                id=id)
        logger.info(f'Change employee. Id: {id}')
    return redirect('/employees')


@app.route('/profile_employee/<user_id>', methods=["POST", "GET"])
def profile_employees(user_id):
    if request.method == 'POST':
        data = select.select_employees(user_id)
        logger.info(f'Show employee profile. Id: {user_id}')
        return render_template('profile_employee.html', data=data)

    logger.debug(f'Not found employee profile. Id: {user_id}')
    return render_template('not_found.html')


@app.route('/delete_employee', methods=["POST", "GET"])
def delete_employee():
    if request.method == "POST":
        if 'delete' in request.form.keys():
            delete.delete_employee(request.form['delete'])
            logger.info(f"Delete employee. Id: {request.form['delete']}")

    return redirect('/employees')


@app.route('/create_employee', methods=["POST", "GET"])
def create_employee():
    if request.method == "POST":
        name = request.form['name']
        specialization = request.form['specialization']
        salary = request.form['salary']
        bonus = request.form['bonus']
        project = request.form['project']
        insert.employees_table(name, specialization, salary, bonus, project)
        logger.info(f'Create new employee')
        return redirect('/employees')
    logger.info(f'Show create employee page')
    return render_template('create_employee.html')


@app.route('/api/v1.0/delete_employee/<int:id>', methods=['DELETE'])
def api_delete_employee(id):
    logger.info(f'Removing an employee using the API')
    return delete.delete_employee(id)


@app.route('/api/v1.0/delete_project/<int:id>', methods=['DELETE'])
def api_delete_project(id):
    logger.info(f'Deleting a project using the API. ID: {id}')
    return delete.delete_project(id)


@app.route('/api/v1.0/info_project/<int:id>', methods=['GET'])
def api_info_project(id):
    logger.info(f'Displaying information about projects using the API. ID: {id}')
    return select.select_project(id)


@app.route('/api/v1.0/info_employee/<int:id>', methods=['GET'])
def api_info_employee(id):
    logger.info(f'Displaying employee information using the API. ID: {id}')
    return select.select_employees(id)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
