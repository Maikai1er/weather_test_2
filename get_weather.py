import requests

response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Valencia'
                        '?unitGroup=metric&key=SSL679LGGZ7LGF7HDVH7NUDSS&contentType=json').json()

get_today_weather = response['days'][0]['hours']
print(get_today_weather)
descriptions = []
for hour in get_today_weather:
    descriptions.append(hour['temp'])

print(descriptions)
