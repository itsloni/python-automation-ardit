import requests
import json


# r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=a3fa169b1c634c3eb19aeb0dac4472c1') # This is a static url API.
# # We'll need to define a function that accepts dynamic user input/ values the user wants to search for
#
# content = r.json()

#print(json.dumps(content, indent=4))
# print(json.dumps(content["articles"][0]["title"], indent=4))
# print(json.dumps(content["articles"][0]["description"], indent=4))
# articles = content['articles']
#
# for article in articles: #used to sieve through the entire article
#     print(f"TITLE: {article['title']},\nDESCRIPTION: {article['description']}")


def get_news(country_abbreviation, api_key='a3fa169b1c634c3eb19aeb0dac4472c1'):
    url = f'https://newsapi.org/v2/top-headlines?country={country_abbreviation}&apiKey={api_key}'
    r = requests.get(url)
    content =r.json()

    articles = content['articles']
    results = []
    for article in articles:
        #results.append(f"TITLE: {article['title']}, DESCRIPTION: {article['description']}")
        result = {
            "TITLE": article['title'],
            "DESCRIPTION" : article['description']
        }
        results.append(result)
    return json.dumps(results, indent=4)

#user_input = input("Drop the country and api_key for the news you want: ")

