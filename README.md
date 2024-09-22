# Python Scraping Project

Este proyecto utiliza Selenium para realizar scraping de datos de páginas web.

## Requisitos

- Docker
- Docker Compose (opcional, si decides usarlo)

## Estructura del Proyecto

python_scraping_project/
├── Dockerfile
├── requirements.txt
├── deploy.sh
├── scraper.py
└── README.md


## Instalación

1. **Clonar el repositorio** (si lo estás utilizando en un repositorio):

   ```bash
   git clone git@github.com:ornelamarinibegue/python-scraping-gcp.git
   cd python_scraping_project


## construir la imagen de Docker

docker build -t python_scraping_project .

## Ejecucion

docker run python_scraping_project

## Descripción del Código
scraper.py: El script principal que contiene la lógica de scraping y contiene el código para procesar los datos obtenidos.
requirements.txt: Lista de dependencias de Python necesarias para el proyecto.
Dockerfile: Archivo que define cómo se construye la imagen de Docker.
deploy.sh: facilita el proceso de construcción, subida y despliegue de la aplicación en Google Cloud Run



## Notas
Asegúrate de que tu Docker esté correctamente configurado y tenga acceso a la GUI si es necesario.
Si experimentas problemas con Chrome al ejecutarlo en Docker, considera configurar el entorno gráfico adecuadamente.


# creación del entorno virtual y activación 
py -m venv venv
.\venv\Scripts\Activate 

## Librerías
py install selenium
py install webdriver-manager
py install pandas

## navegar por el HTML de la pagina (comando inspeccionar)

Navegar a la URL de Yogonet.
Extraer los datos necesarios de cada artículo:
El título (normalmente se encuentra dentro de etiquetas como <h2>).
El kicker (puede estar dentro de un div o una clase específica que debes inspeccionar).
La imagen (extrae el atributo src de la etiqueta <img>).
El link (extrae el atributo href de la etiqueta <a>).
y luego guardarlo en cada variable segun el código del archivo scraper.py

## Completar algunas variables
your-project-id --> completar con el id del proyecto que creamos en Google cloud para el challenge (archivo deploy.sh line 15)
your-project-id.your-dataset-id.your-table-id --> completar con el id del proyecto, el data set y nombre de table que creamos en Big query para almacenar los datos (arcivo scraper.py line 51)

#   p y t h o n - s c r a p i n g - g c p 
 
 
