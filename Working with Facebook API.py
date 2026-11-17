import requests
import json

url = "https://graph.facebook.com/v27.0/me?fields=id%2Cname%2Cemail%2Cpicture&access_token=EAA7VKptesBgBTJEHTLGFxbPxwZApNdLhBwxAIMpGfCOsoZAMRYgCVRntUhEj7zjPQkJjxunjAQFZCZAqQSlp3aEwO847GZAl6ZCeNwNMh8padE6tXFtiOSEVZBAMfNLJZClED9bK2rY4EGrsB6G3UMihaVabGrZC3IgZCbMZBAXANEJuc8tUB0pBzzYq8478uJff1Vt93f5FT6Ro6DQe9HQKT0iDyuzq9OUaZBLEbIt2"

response = requests.get(url)

data = response.json()
image_url = data["picture"]["data"]["url"]

image_byte = requests.get("https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=122104099875549027&height=50&width=50&ext=1797520900&hash=Afu4vB1rNz_wZtzj_XeDtFtl")
pure_image_byte = image_byte.content

with open ("image.jpg", "wb") as file:
    file.write(pure_image_byte)