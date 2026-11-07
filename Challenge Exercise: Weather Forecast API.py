import requests
import pandas
import json

results= []
def get_weather_updates(city, api_key='b819eb6c53c417a8d4ba246a34ec6bff'):
    r = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric')
    content = r.json()

    for weather_info in content['list']:
        result = {
            'City': f'{city}',
            'Time': f'{weather_info['dt_txt']}',
            'Temperature': f'{weather_info['main']['temp']}',
            'Condition': f'{weather_info['weather'][0]['description']}'
        }
        results.append(result)

    #return results

    easy_read = json.dumps(results, indent=4) #remember that this converts yoy input ot a string
    return easy_read

        # return content

user_input = (get_weather_updates("Calgary"))
print(user_input)

with open('data.txt', 'a') as output_data_file:
    output_data_file.write(user_input)

# df = pandas.DataFrame(user_input)
# df.to_txt('data.txt')