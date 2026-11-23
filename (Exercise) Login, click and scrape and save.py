from selenium import webdriver
import time
from datetime import datetime

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.timeanddate.com/worldclock/nigeria/lagos")

    return driver


def clean_text(text):
    output = int(text.split(":")[2])
    return output


def auto_file_creator(cleaned_text):
    output_time = datetime.now()
    output_time = output_time.strftime("%Y-%m-%d.%H-%M-%S")
    with open (f"{output_time}.txt", "w") as file:
        return file.write(cleaned_text)

def main():
    driver = get_driver()
    while True:
        element = driver.find_element(by="id", value="ct")
        cleaned_text = str(clean_text(element.text))
        auto_file_creator(cleaned_text)
        time.sleep(2)

main()
