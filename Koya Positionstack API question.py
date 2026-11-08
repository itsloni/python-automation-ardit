import requests
import json

first_address = []
def postion_address(latitude, longitude, api_key='6e0117bf0feb363c616079ac9cad1e49'):
    r = requests.get(
        f'https://api.apilayer.net/positionstack/v1/reverse?access_key={api_key}&query={latitude},{longitude}')
    content = r.json()

    print(content['data'][0])
    # print(address)
    # first_address.append(address)

    # style = json.dumps(content, indent=4)
    # return style
    # 6e0117bf0feb363c616079ac9cad1e49


print(postion_address('6.4410', '3.5357'))
# print(first_address)
