#Selenium is a 3rd party Python library that is used to automate browser actions including things like
# clicking on a link, copying text, or login to website, entering username and password and so on etc
from selenium import webdriver

def get_driver():
    #The options below are set to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars') # This are flags and the "disable-infobars" will disable the bars in websites that display like memory and some info and it could confuse the cursor when webdriver works
    options.add_argument('start-maximized') #This is good cause like some webpages makes the font and areas in the site smaller when you try to access it so the 'start-maximized' works well.
    options.add_argument('disable-dev-shm-usage') #This option is to avoid issues that occur when you interact with the browser on a linux computer
    options.add_argument("no-sandbox") #so webpages for security do what we call sandboxing but if we want our webdriver to have more priviledges we use this option so sandboxing is disabled
    options.add_experimental_option("excludeSwitches", ["enable_automation"]) #This '.add_experimental_option' is used so selenium can avoid detection from web browsers.
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver
def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/p[2]")
    return element.text

print(main())

