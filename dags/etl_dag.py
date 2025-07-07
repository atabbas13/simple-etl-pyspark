from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='spark_etl_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['spark', 'etl'],
) as dag:

    run_etl = DockerOperator(
        task_id='run_spark_etl',
        image='bitnami/spark:3.5',
        container_name='spark_etl_runner',
        command='spark-submit --jars /opt/spark/jars/postgresql-42.6.0.jar /app/main.py',
        auto_remove=True,
        volumes=[
            '/full/path/to/your/project:/app',
            '/full/path/to/your/project/jars:/opt/spark/jars'
        ],
        network_mode='bridge'  # or 'host' if needed
    )

    run_etl