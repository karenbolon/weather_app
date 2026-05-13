import requests
from twilio.rest import Client
import os

api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
kay = os.getenv("KAY")
miks = os.getenv("MIKS")
twilio_num = os.getenv("TWILIO")

print("API_KEY loaded?", bool(api_key))
print("ACCOUNT_SID loaded?", bool(account_sid))
print("AUTH_TOKEN loaded?", bool(auth_token))
print("TWILIO loaded?", bool(twilio_num))

berlin_params = {
    "lat": 52.520008,
    "lon": 13.404954,
    "cnt": 4,
    "appid": api_key,
    "units": "metric"
    }

ingleheim_params = {
    "lat": 49.9779,
    "lon": 8.0723,
    "appid": api_key,
    "cnt": 4,
    "units": "metric"
}

def get_weather_data():
    weather_response = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                                    params=berlin_params)
    weather_response.raise_for_status()
    weather_data = weather_response.json()["list"]

    rain = False
    for data in weather_data:
        if int(data['weather'][0]['id']) < 800:
            rain = True
    if rain:
        client = Client(account_sid, auth_token)

        recipients = [kay, miks]

        for r in recipients:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body="It's going to rain today. Remember to bring an umbrella",
                to = r
                )
            print(message.status)

get_weather_data()