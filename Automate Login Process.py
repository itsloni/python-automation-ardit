#Automating Login in Process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
load_dotenv()

my_password = os.getenv("outlook_password")
def get_driver():
    #The options below are set to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.pythonanywhere.com/login/")
    return driver
def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_auth-username").send_keys("itsloni") # So because we're trying to log-in into a website instead of using 'xpath' we can use 'id'  its more robust and efficient
  # note the above driver.find is not in a variable like teh other one we did in scraping cause right now we're not scraping but rather we're trying to access a  website
    time.sleep(2)
    driver.find_element(by="id", value="id_auth-password").send_keys(my_password + Keys.RETURN)# The "+ Keys.RETURN" is attribute of the Keys object imported to click the login when the user_name and password has been done.
    print(driver.current_url)# This is to  just have a printed putput showing the url when you log-in to just be sure . it's for you. If the log-in was not successful the url WILL NOT be printed.
print(main())

