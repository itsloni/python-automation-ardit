# This deals with scraping Values that are constantly changing from a website
#Selenium is a 3rd party Python library that is used to automate browser actions including things like
# clicking on a link, copying text, or login to website, entering username and password and so on etc
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
    driver.get("https://www.timeanddate.com/")
    return driver

def clean_text(text):
    #This is where we clean the text to extract exactly what we want.
    output = int(text.split(":")[1])
    return output

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="//*[@id='clk_box']")
    return clean_text(element.text)

print(main())

