from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests, json

# Create your views here.
def LA_view(request):
    
    api_key = "super_secret_key"
    url = "http://api.weatherapi.com/v1/current.json?key=" + api_key + "&q=Los Angeles"

    response = requests.get(url)

    json_data = response.json()

    location = json_data["location"]["name"], json_data["location"]["region"], json_data["location"]["country"]
    temp_f = json_data["current"]["temp_f"]
    condition = json_data["current"]["condition"]["text"]


    return HttpResponse(f"Name: {location} <br> Temp (F): {temp_f} <br>Conditions: {condition} <br> <a href=../home_view> home_view </a>")

def home_view(request):
    str1 = "yurr"
    context = {"str1":str1}
    return render(request, "weather/home.html", context)
