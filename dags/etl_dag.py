from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='spark_etl_pipeline',
    default_args=default_args,
    schedule_interval=None,  # Set to '0 12 * * *' for daily at noon
    catchup=False,
    tags=['spark', 'etl'],
    description='Run PySpark ETL job inside Docker Spark container'
) as dag:

    run_etl = BashOperator(
        task_id='run_spark_etl',
        bash_command='docker exec spark spark-submit --jars /opt/spark/jars/postgresql-42.6.0.jar /app/main.py'
    )

    run_etl