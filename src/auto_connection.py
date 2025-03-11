from selenium import webdriver
import time

# Streamlit アプリのURL
STREAMLIT_APP_URL = "https://your-streamlit-app-url.streamlit.app"

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # GUIなしで実行
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(STREAMLIT_APP_URL)
        print(f"Accessed: {STREAMLIT_APP_URL}")
        time.sleep(30)  # 30秒間滞在（適宜変更）
        print("App is awake!")
    except Exception as e:
        print(f"Error accessing the app: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    while True:
        open_browser()
        print("Sleeping for 30 minutes before next access...")
        time.sleep(60 * 30)  # 30分ごとに実行
