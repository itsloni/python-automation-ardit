import requests
import json
import pandas

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
    return json.dumps(results, indent=4) # This is used to print a neat and smooth dictionary in list but ultimately
    # converts it to a string which can't be used or converted to a DataFrame for csv file.
    #return results # This was returned because it is a pure list of dictionaries not a string which json.dumps converts its content to.

user_input = get_news("us")
print(user_input)