from google.cloud import bigquery

def test_bigquery_connection():
    try:
        # Crear un cliente de BigQuery
        client = bigquery.Client()
        
        # Listar los datasets en el proyecto
        datasets = client.list_datasets()  # Llama a la API para obtener los datasets
        print("Datasets disponibles en el proyecto:")
        for dataset in datasets:
            print(f"- {dataset.dataset_id}")

    except Exception as e:
        print(f"Error al conectar a BigQuery: {e}")

if __name__ == "__main__":
    test_bigquery_connection()
