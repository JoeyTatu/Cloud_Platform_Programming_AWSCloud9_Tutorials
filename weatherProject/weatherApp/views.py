from django.shortcuts import render

# Create your views here.

import urllib.request
import json

app_name = 'weatherApp'

def index(request):
    api_key = 'c280f4a8ccc711c7ca89ff8fccc01431'
    if request.method == "POST":
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + api_key).read()
        
        list_of_data = json.loads(source)
        
        data = {
            "countey_code": str(list_of_data['sys']['country']),
            "coordinates" : str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            "temp"        : str(list_of_data['main']['temp']) + '°C',
            "pressure"    : str(list_of_data['main']['pressure']) + 'hPa',
            "humidity"    : str(list_of_data['main']['humidity']) + '%',
            "main"        : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon"        : list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}
        
    return render(request, "main/index.html", data)
        