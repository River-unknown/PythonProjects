import requests
import json

city = input("Enter your city: ")
url = f'https://api.weatherapi.com/v1/current.json?key=7f9e0a5f02974916ab8183124241303&q={city}'
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
