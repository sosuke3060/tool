from selenium import webdriver
import time

# Streamlit アプリのURL
STREAMLIT_APP_URL = "https://sosuke3060-recipe-ai-srcapp-openai-nhywmb.streamlit.app/"

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # GUIなしで実行
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(STREAMLIT_APP_URL)
        time.sleep(30)  # 30秒間滞在（適宜変更）
    finally:
        driver.quit()

if __name__ == "__main__":
    while True:
        open_browser()
        time.sleep(60 * 30)  # 30分ごとに実行
