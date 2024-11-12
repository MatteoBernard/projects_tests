from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


class Browser:
    def __init__(self):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--start-fullscreen")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        driver_path = os.path.join(current_dir, "..", "drivers", "chromedriver130.exe")

        if not os.path.exists(driver_path):
            raise FileNotFoundError(f"Driver not found at {driver_path}")

        self.driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    def get(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()
