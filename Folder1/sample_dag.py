from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils import timezone
from datetime import timedelta
from dateutil import parser
​
dag = DAG(
    dag_id='sid_dags',
    start_date=parser.isoparse('2023-10-17T08:30:29Z').replace(tzinfo=timezone.utc),
    schedule_interval='*/2 * * * *',
    catchup=True,
    is_paused_upon_creation=False,
    default_args={
        'owner': 'dexssoadmin',
    },
)
​
def function_c9fa6937():
    print("Starting the dag, user is here")
​
python_1 = PythonOperator(
    python_callable=function_c9fa6937,
    task_id='python_1',
    dag=dag,
)
​
def function_552dd2f8():
    print("Ending a dag, user is here")
​
python_2 = PythonOperator(
    python_callable=function_552dd2f8,
    task_id='python_2',
    dag=dag,
)
​
def function_ead049c6():
    print("med job")
​
python_3 = PythonOperator(
    python_callable=function_ead049c6,
    task_id='python_3',
    dag=dag,
)
​
python_2 << [python_3]
python_3 << [python_1]
