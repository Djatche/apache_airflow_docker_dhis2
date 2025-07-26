from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from dhis2 import Api
import pandas as pd

# Configuration API DHIS2
DHIS2_URL = "https://play.im.dhis2.org/stable-2-42-1"
DHIS2_USERNAME = "admin"
DHIS2_PASSWORD = "district"

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def import_data_from_dhis2():
    # Connexion à DHIS2
    api = Api(DHIS2_URL, DHIS2_USERNAME, DHIS2_PASSWORD)

    # Exemple : obtenir les données de programme
    data = api.get('organisationUnits').json()
    data = data['organisationUnits']

    #pager = data['pager']

    #print(pager)
    # Create DataFrame and rename columns
    df = pd.DataFrame(data)[["displayName", "id"]].rename(columns={"displayName": "name"})

    # print(df)

    # Sauvegarde locale pour test (tu peux remplacer par PostgreSQL)
    df.to_csv('/opt/airflow/data/ou.csv', index=False)
    print("Export terminé :", df.head())

with DAG(
    dag_id='dhis2_import_dag',
    default_args=default_args,
    description='Importation des données depuis DHIS2 API',
    schedule='@daily',
    start_date=datetime(2025, 7, 25),
    catchup=False,
    tags=['dhis2', 'import'],
) as dag:

    import_task = PythonOperator(
        task_id='import_dhis2_data',
        python_callable=import_data_from_dhis2
    )

    import_task
