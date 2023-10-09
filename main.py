import requests
import json

# 例: 佐賀県 伊万里のIDは410020
city_id = 410020

url = f"https://weather.tsukumijima.net/api/forecast/city/{city_id}"
response = requests.get(url)
data = response.json()
tomorrow_forecast = data['forecasts'][1]  # 0: 今日, 1: 明日, 2: 明後日
print(f"Date: {tomorrow_forecast['date']}")
print(f"Weather: {tomorrow_forecast['telop']}")
