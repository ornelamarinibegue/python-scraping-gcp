from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

def process_data(data):
    df = pd.DataFrame(data)
    
    # Calcular métricas
    df['word_count'] = df['title'].apply(lambda x: len(x.split()))
    df['char_count'] = df['title'].apply(len)
    df['capital_words'] = df['title'].apply(lambda x: [word for word in x.split() if word[0].isupper()])
    
    # Aquí podrías insertar df en BigQuery o retornarlo para uso posterior
    return df

def main():
    # Configuración del WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Opcional: ejecutar sin interfaz gráfica
    #options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Definición de la URL
    url = "https://www.yogonet.com/international/"
    driver.get(url)

    # Extraer los datos necesarios
    articles = driver.find_elements(By.CLASS_NAME, "article")  # no hice a tiempo Cambia esto según la estructura del HTML
    print(articles)
    data = []
    driver.quit()

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
            print(f"Error al procesar el artículo: {e}"  
            )

    driver.quit()

    # Procesar los datos
    df = process_data(data)
    print(df)

if __name__ == "__main__":
    main()
