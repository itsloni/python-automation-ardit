from flask import Flask, jsonify

from bs4 import BeautifulSoup # This is a web scraping module/library that contains a lot of executabkle programs to scrape webpages(webapps)/sites
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).content

app = Flask(__name__) # THIS '__name__' IS A VERY SPECIAL VARIABLE THAT HOLDS THE STRING OF THE SCRIPT __main__

@app.route('/')
def home():
    return "<h1>Currency Rate Loni's API</h1> <p>Example URL: /api/v1/usd-eur</p> <p> What are you waiting for? LFG </p>"

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):


app.run(host='0.0.0.0')
