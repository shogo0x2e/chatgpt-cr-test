import requests
import json

def func(city_id):
    url = f"https://weather.tsukumijima.net/api/forecast/city/{city_id}"
    response = requests.get(url)
    data = response.json()
    tomorrow_forecast = data['forecasts'][1]  # 0: 今日, 1: 明日, 2: 明後日
    print(f"Date: {tomorrow_forecast['date']}")
    print(f"Weather: {tomorrow_forecast['telop']}")

func(410020)