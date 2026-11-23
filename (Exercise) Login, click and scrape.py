from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

my_password = os.getenv("outlook_password")


def get_drivers():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    drivers = webdriver.Chrome(options=options)
    drivers.get("https://www.pythonanywhere.com/login/")
    return drivers
# get_drivers()

def main():
    drivers = get_drivers()
    drivers.find_element(by="id", value="id_auth-username").send_keys("itsloni")
    time.sleep(2)
    drivers.find_element(by="id", value="id_auth-password").send_keys(my_password + Keys.RETURN)
    time.sleep(2)
    drivers.find_element(by="id", value="id_tasks_link").click()
    time.sleep(2)
    scraped_element = drivers.find_element(by="id", value="id_cpu_usage_information")
    final_scraped_element = scraped_element.text.replace(" More Info", "").strip()
    return final_scraped_element

print(main())