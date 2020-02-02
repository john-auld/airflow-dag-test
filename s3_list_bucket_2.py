from airflow.models import DAG
from airflow.contrib.operators.s3_list_operator import S3ListOperator
from datetime import datetime

with DAG(dag_id='s3_list_bucket',
         schedule_interval=None,
         start_date=datetime(2019, 6, 7)) as dag:

    s3_file = S3ListOperator(
        task_id='list_3s_files',
        bucket='airflow-dag-test-bucket-2',
        prefix='test',
        delimiter='/',
        aws_conn_id='aws_default'
    )
