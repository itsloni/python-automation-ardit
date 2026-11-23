# Web scraping using beautiful soup.. note that Beautiful soup is limit to scrape only html can convert javascript or other langs.
from bs4 import BeautifulSoup
import requests


def get_currency(input_currency, output_currency):
    url = f"https://x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt title-36 text-content-base tabular-nums sm:title-48").get_text()
    print(rate)

get_currency("USD", "GBP")