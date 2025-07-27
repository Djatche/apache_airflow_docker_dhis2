\# Planification et orchestration pour l'automatisation des tâches dans le DHIS2 (niveau district de santé)

\# Outils utilisés:
## Apache/airflow
## Docker
## Dhis2.py
## pandas
## pyyaml>6.0.0



\# Quelques opérations menées

* Un Dockerfile a été créé à partir de l'image "apache/airflow:3.0.2-python3.11" et nous avons inclut pip install requirements.txt
* Le docker-compose.yaml a été récupérer du site apache/airflow
* Dans ce docker-compose.yaml on a commenté l'image et decommenté le build .
* On ajouter un volume /data: /opt/airflow/data en plus de ceux existant déjà à savoir logs, dags, config, plugins.
* Dans l'environnment virtuel, on a lancé pip install -r requirements.txt
* Pour versionner les fichiers logs, config, .env et venv ont été ignoré grâce au fichier .gitignore



\## Que fait ce workflow dans le fichier python my\_dag\_dhis2.py:
Création de la fonction "import\_data\_from\_dhis2" qui va faciliter:

* La récupération des données d'une plateforme DHIS2 sous format json de toutes les unités d'organisation (On a voulu faire simple) grâce au package DHIS2.py.
* La création d'un dataframe à l'aide de pandas.
* La sauvegarde sous forme de fichier csv "ou.csv".

Ce workflow représenté par le DAG créé avec le dag\_id "dhis2\_import\_dag" a une seule tâche.
Ce workflow est sensé s'exécuter quotidiennement à 24 h et ceci 1 jour après la date de début (start\_date)
Cette tâche est un python opérator dont le task\_id est "import\_dhis2\_data".
Cette tâche execute la fonction décrite plus haut grâce au python\_callable.

\# Conclusion
Nous avont planifié, monitorer et orchestré un workflow (un flux de travail) automatisé. Les districts de santé peuvent tirer profit de ces compétences mais à condition de disposer des ressources humaines (data engineer).

