import plotly
import plotly.graph_objs as go
import plotly.express as px
import sqlite3
import numpy as np
import pandas as pd
import pymysql
from config import host, user, password, database



def project_graph():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select * from projects_table')
            data = cur.fetchall()
    name = [dat[1] for dat in data]
    employees = [dat[5] for dat in data]
    fig = px.histogram(x=name, y=employees)
    fig.update_layout(xaxis_title="Employees", yaxis_title="Project")
    fig = fig.to_html(full_html=False)
    return fig


def salary_graph():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select * from employees_table')
            data = cur.fetchall()
    name = [dat[1] for dat in data]
    salary = [dat[3] for dat in data]
    fig = px.histogram(x=name, y=salary)
    fig.update_layout(xaxis_title="Name", yaxis_title="Salary")
    fig = fig.to_html(full_html=False)

    return fig


def bonus_graph():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    with connection:
        with connection.cursor() as cur:
            cur.execute('Select * from employees_table')
            data = cur.fetchall()
    name = [dat[1] for dat in data]
    salary = [dat[4] for dat in data]
    fig = px.histogram(x=name, y=salary)
    fig.update_layout(xaxis_title="Name", yaxis_title="Bonus")
    fig = fig.to_html(full_html=False)
    return fig
