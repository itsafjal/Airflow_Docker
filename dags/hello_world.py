from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.models import DagBag, DagModel, DagRun, TaskInstance
from airflow import AirflowException
from sqlalchemy.orm.session import Session
from airflow.utils.state import State
import re
import os
from subprocess import call
from airflow.models import Variable
import time
import uuid
import  fileinput
import requests
from datetime import datetime, timedelta
import io


default_args = {
    'owner': 'Afzal',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 11),
    'email': ['Youmail@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

sql_search_path = Variable.get("sql_template_path")

with DAG(dag_id='test_dag', default_args=default_args, schedule_interval=None) as dag:

    def helloWorld():
        print("Hello World function for airflow")

    helloWorldOp= PythonOperator(task_id='print_hello_world', retries=3,python_callable=helloWorld, dag=dag)

    helloWorldOp




 