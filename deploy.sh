#!/bin/bash

# Script para construir el contenedor Docker y desplegar en Cloud Run

# Construir la imagen
docker build -t python_scraping_project .

# Autenticar con GCR
gcloud auth configure-docker

# Etiquetar la imagen
docker tag python_scraping_project gcr.io/your-project-id/python_scraping_project

# Subir la imagen a GCR
docker push gcr.io/your-project-id/python_scraping_project

# Desplegar en Cloud Run
gcloud run deploy python_scraping_project --image gcr.io/your-project-id/python_scraping_project --platform managed
