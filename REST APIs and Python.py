import requests
import json

r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=a3fa169b1c634c3eb19aeb0dac4472c1')

content = r.json()

#print(json.dumps(content, indent=4))
# print(json.dumps(content["articles"][0]["title"], indent=4))
# print(json.dumps(content["articles"][0]["description"], indent=4))
articles = content['articles']

for article in articles: #used to sieve through the entire article
    print(f"TITLE: {article['title']},\nDESCRIPTION: {article['description']}")