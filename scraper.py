from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

def extract_data(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    articles = driver.find_elements(By.CLASS_NAME, "article")
    data = []
    for article in articles:
        try:
            title = article.find_element(By.CLASS_NAME, "titulo").text
            kicker = article.find_element(By.CLASS_NAME, "div").text
            image = article.find_element(By.CLASS_NAME, "img").get_attribute("src")
            link = article.find_element(By.TAG_NAME, "a").get_attribute("href")

            data.append({
                "title": title,
                "kicker": kicker,
                "image": image,
                "link": link
            })
        except Exception as e:
            print(f"Error al procesar el artículo: {e}")

    driver.quit()
    return data

def process_data(data):
    df = pd.DataFrame(data)
    # Calcular métricas
    df['word_count'] = df['title'].apply(lambda x: len(x.split()))
    df['char_count'] = df['title'].apply(len)
    df['capital_words'] = df['title'].apply(lambda x: [word for word in x.split() if word[0].isupper()])
    return df

def main():
    url = "https://www.yogonet.com/international/"
    data = extract_data(url)
    df = process_data(data)
    print(df)

    # Load the processed data into BigQuery
    from google.cloud import bigquery
    client = bigquery.Client()
    table_id = "your-project-id.your-dataset-id.your-table-id"
    job = client.load_table_from_dataframe(df, table_id)
    job.result()

if __name__ == "__main__":
    main()
