from django.shortcuts import render
import urllib.request
import json
from django.contrib import messages
# Create your views here.
def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        if city is None:
            messages.info(request, "City does not exist")
        else:
            res = urllib.request.urlopen('http://api.weatherapi.com/v1/current.json?key=1a3b267f16c4482d8e3221313231809&q='+city+'&aqi=no')
            json_data = json.load(res)
            stats = {
                'country': str(json_data["location"]["name"]) + ", " + str(json_data["location"]["country"]),
                'current_temp_f': str(json_data["current"]["temp_f"]),
                'current_temp_c': str(json_data["current"]["temp_c"]), 
                'icon': str(json_data["current"]["condition"]["icon"]),
                'condition': str(json_data["current"]["condition"]["text"])
            }
    else:
        stats = ''
    return render(request, 'home.html', stats)