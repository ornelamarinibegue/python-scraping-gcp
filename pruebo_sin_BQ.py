from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def extract_data(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Esperar a que los artículos sean cargados
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "contenedor_dato_modulo"))
    )

    articles = driver.find_elements(By.CLASS_NAME, "contenedor_dato_modulo")
    data = []
    for article in articles:
        try:
            # Extraer el kicker (volanta)
            kicker = article.find_element(By.CLASS_NAME, "volanta").text
            
            # Extraer el título
            title_element = article.find_element(By.CLASS_NAME, "titulo")
            title = title_element.text

            # Extraer el link del artículo
            link = title_element.find_element(By.TAG_NAME, "a").get_attribute("href")
            
            # Extraer la imagen
            image = article.find_element(By.TAG_NAME, "img").get_attribute("src")
            
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

    # Guarda el DataFrame en un archivo CSV en lugar de cargarlo a BigQuery
    df.to_csv("datos_yogonet.csv", index=False)  # Guarda el DataFrame en un archivo CSV
    print("Datos guardados en 'datos_yogonet.csv'.")

if __name__ == "__main__":
    main()
