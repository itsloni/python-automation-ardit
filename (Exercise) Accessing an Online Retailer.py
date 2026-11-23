from selenium import webdriver
import os
import time
from dotenv import load_dotenv
load_dotenv()

my_email = os.getenv("gmail_email")
my_password = os.getenv("titan22_password")

url = "https://titan22.com/account/login"

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-ysage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blinking-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
