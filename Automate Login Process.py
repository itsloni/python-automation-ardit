#Automating Login in Process
from selenium import webdriver

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
    element = driver.find_element(by="id", value="id_auth-username") # So because we're trying to login into a website instead of using 'xpath' we can use 'id'  its more robust and efficient
    return element.text

print(main())

