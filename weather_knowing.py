# enter city name
import json
import requests

api_key = "a10d14f7bfe7cb43c38b24a42e91ca45"
user_input = input("city name\n")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")
weather = weather_data.json()
print(weather)
# if weather_data.json()['cod'] == '404':
#     print("No city found")
# else:
#     weather = weather_data.json()['weather'][0]['main']
#     tempr = round(weather_data.json()['main']['temp'])
#     print(f"the weather in {user_input} is: {weather}")
#     print(f"the temperature in {user_input} is: {tempr} degree F")


