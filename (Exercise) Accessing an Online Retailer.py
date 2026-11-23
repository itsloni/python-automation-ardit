from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    driver.get(url)
    time.sleep(3)
    return driver
# get_driver()
def main():
    driver = get_driver()
    driver.find_element(by="id", value="CustomerEmail").send_keys(my_email)
    driver.find_element(by="id", value="CustomerPassword").send_keys(my_password + Keys.RETURN)
    driver.find_element(by="", value="").click()
main()