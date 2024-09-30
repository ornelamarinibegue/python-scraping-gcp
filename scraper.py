from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from google.cloud import bigquery

def extract_data(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Espera hasta que los artículos estén presentes
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".contenedor_dato_modulo"))
        )
        
        articles = driver.find_elements(By.CSS_SELECTOR, ".contenedor_dato_modulo")
        data = []

        for article in articles:
            # Inicializa variables por defecto
            kicker = "No disponible"
            title = "No disponible"
            link = "No disponible"
            image = "No disponible"

            # Extraer el kicker (volanta) si existe
            try:
                kicker = article.find_element(By.CSS_SELECTOR, ".volanta").text
            except NoSuchElementException:
                print("Kicker no disponible para este artículo.")

            # Extraer el título
            try:
                title_element = article.find_element(By.CSS_SELECTOR, "h2.titulo")
                title = title_element.text
            except NoSuchElementException:
                print("Título no disponible para este artículo.")

            # Extraer el link del artículo
            try:
                link = title_element.find_element(By.TAG_NAME, "a").get_attribute("href")
            except NoSuchElementException:
                print("Link no disponible para este artículo.")

            # Extraer la imagen
            try:
                image = article.find_element(By.CSS_SELECTOR, "div.imagen img").get_attribute("src")
            except NoSuchElementException:
                print("Imagen no disponible para este artículo.")

            # Agregar datos extraídos a la lista
            data.append({
                "title": title,
                "kicker": kicker,
                "image": image,
                "link": link
            })
    except TimeoutException:
        print("No se encontraron artículos en la página dentro del tiempo límite.")
    finally:
        driver.quit()

    return data

def process_data(data):
    df = pd.DataFrame(data)
    # Calcular métricas
    df['word_count'] = df['title'].apply(lambda x: len(x.split()))
    df['char_count'] = df['title'].apply(len)
    df['capital_words'] = df['title'].apply(lambda x: [word for word in x.split() if word[0].isupper()])
    return df

def create_bigquery_table_if_not_exists(table_id):
    client = bigquery.Client()

    # Verificar si la tabla ya existe
    try:
        client.get_table(table_id)
        print(f"La tabla {table_id} ya existe.")
    except Exception as e:
        print(f"La tabla {table_id} no existe, se procederá a crearla.")
        # Definir el esquema
        schema = [
            bigquery.SchemaField("title", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("kicker", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("image", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("link", "STRING", mode="NULLABLE"),
        ]
        
        # Crear la tabla
        table = bigquery.Table(table_id, schema=schema)
        table = client.create_table(table)  # API request
        print(f"Tabla {table_id} creada satisfactoriamente.")

def load_data_to_bigquery(df, table_id):
    create_bigquery_table_if_not_exists(table_id)  # Crear tabla si no existe

    client = bigquery.Client()
    job = client.load_table_from_dataframe(df, table_id)
    job.result()  # Esperar a que el trabajo de carga se complete
    print(f"Datos cargados en la tabla {table_id}.")

def main():
    url = "https://www.yogonet.com/international/"
    data = extract_data(url)
    df = process_data(data)
    print(df)

    # Define tu ID de tabla (proyecto.dataset.tabla)
    table_id = "your-project-id.your-dataset-id.your-table-id"  # Coloca tu project_id y dataset aquí

    # Cargar los datos procesados en BigQuery
    load_data_to_bigquery(df, table_id)

if __name__ == "__main__":
    main()
