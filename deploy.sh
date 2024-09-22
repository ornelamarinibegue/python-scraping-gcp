#!/bin/bash

# Script para construir el contenedor Docker y desplegar en Cloud Run

# Construir la imagen
docker build -t python_scraping_project .

# Aquí puedes añadir el comando para subir a un repositorio de artefactos

# Desplegar en Cloud Run
gcloud run deploy python_scraping_project --image gcr.io/your-project-id/python_scraping_project --platform managed
