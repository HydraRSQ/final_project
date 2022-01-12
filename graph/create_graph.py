import plotly
import plotly.graph_objs as go
import plotly.express as px
import sqlite3
import numpy as np
import pandas as pd


def project_graph():
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    data = cur.execute('Select * from projects_table').fetchall()
    name = [dat[1] for dat in data]
    employees = [dat[6] for dat in data]
    fig = px.histogram(x=name, y=employees)
    fig.update_layout(xaxis_title="Employees", yaxis_title="Project")
    fig = fig.to_html(full_html=False)
    return fig


def salary_graph():
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    data = cur.execute('Select * from employees_table').fetchall()
    name = [dat[1] for dat in data]
    salary = [dat[3] for dat in data]
    fig = px.histogram(x=name, y=salary)
    fig.update_layout(xaxis_title="Name", yaxis_title="Salary")
    fig = fig.to_html(full_html=False)

    return fig


def bonus_graph():
    con = sqlite3.connect('Service/base.db')
    cur = con.cursor()
    data = cur.execute('Select * from employees_table').fetchall()
    name = [dat[1] for dat in data]
    salary = [dat[4] for dat in data]
    fig = px.histogram(x=name, y=salary)
    fig.update_layout(xaxis_title="Name", yaxis_title="Bonus")
    fig = fig.to_html(full_html=False)
    return fig
