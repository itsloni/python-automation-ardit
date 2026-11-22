from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

def get_drivers():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    drivers = webdriver.Chrome()
    drivers.get("https://www.pythonanywhere.com/login/")



def main():
    drivers = get_drivers()
    drivers