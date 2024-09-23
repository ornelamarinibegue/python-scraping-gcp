# Web Scraping and Ingest Challenge

## Descripción General
Este repositorio contiene un script en Python que realiza tareas de web scraping, procesamiento de datos y despliegue utilizando Selenium, Pandas y Google Cloud BigQuery. El script está Dockerizado y puede desplegarse en Google Cloud Run utilizando un script bash.

## Estructura del Proyecto

python_scraping_project/  

├── Dockerfile : Archivo que define cómo se construye la imagen de Docker.  

├── requirements.txt : Lista de dependencias de Python necesarias para el proyecto.  

├── deploy.sh : facilita el proceso de construcción, subida y despliegue de la aplicación en Google Cloud Run  

├── scraper.py : El script principal que contiene la lógica de scraping y contiene el código para procesar los datos obtenidos.  

└── README.md

## Configuración

### Requisitos Previos
Docker instalado en tu sistema  
Cuenta de Google Cloud con BigQuery habilitado  
Google Cloud CLI instalado en tu sistema  

### Librerías
pip install selenium  
pip install webdriver-manager  
pip install pandas  

### creación del entorno virtual y activación 
py -m venv venv  
.\venv\Scripts\Activate 

### Ejecución del Script
Clona este repositorio en tu máquina local:  
git clone git@github.com:ornelamarinibegue/python-scraping-gcp.git  
or  
git clone https://github.com/ornelamarinibegue/python-scraping-gcp.git  

Navega al directorio del repositorio.  
cd python-scraping-project/  
Ejecuta el comando docker build -t python_scraping_project . para construir la imagen Docker.  
Ejecuta el comando docker run python_scraping_project para ejecutar el contenedor Docker.

### Despliegue en Cloud Run
Ejecuta el comando bash deploy.sh para desplegar la imagen Docker en Cloud Run.

## Configuración

### Variables de Entorno
GOOGLE_CLOUD_PROJECT: ID de tu proyecto de Google Cloud  
BIGQUERY_DATASET: ID del dataset de BigQuery  
BIGQUERY_TABLE: ID de la tabla de BigQuery  

### Integración con BigQuery
El script utiliza la biblioteca google-cloud-bigquery para interactuar con BigQuery. Debes tener configurada la variable de entorno GOOGLE_APPLICATION_CREDENTIALS con la ruta al archivo de la clave de tu cuenta de servicio.

## Desarrollo
Historial de Commits
Por favor, consulta el historial de commits para obtener un registro detallado de los cambios realizados en el código.

Contribuciones
¡Las contribuciones son bienvenidas! Por favor, haz un fork de este repositorio y envía un pull request con tus cambios.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.










