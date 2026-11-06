import requests
import json
import pandas


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
    #return json.dumps(results, indent=4) # This is used to print a neat and smooth dictionary in list but ultimately
    # converts it to a string which can't be used or converted to a DataFrame for csv file.
    return results # This was returned because it is a pure list of dictionaries not a string which json.dumps converts its content to.

user_input = get_news("us")
print(user_input)
df = pandas.DataFrame(user_input)
df.to_csv('listofdicts_output.csv')


