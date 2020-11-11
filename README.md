# Setup airflow in docker local 

Requirement

1. Linux/Mac OS
2. Docker


Step1. Pull docker image

      docker pull puckel/docker-airflow

Step2.
     
     docker run -d -p 8080:8080 puckel/docker-airflow webserver

Step3
     clone this repo into your local
     
Step4
     docker run -d -p 8080:8080 -v /path/to/dags/on/your/local/machine/:/usr/local/airflow/dags  puckel/docker-airflow webserver
     
     
Open your browswer localhost:8080
     
