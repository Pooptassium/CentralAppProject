from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    return render(request, "youtube/home.html")

def servercall(request):
    key = request.POST["text"]

    url = "https://googleapis.com/youtuve/v3/videos"

    params = {
        "part" : "snippet,statistics",
        "chart" : "mostPopular",
        "regionCode" : "US",
        "maxResults" : 10,
        "key" : key
    }

    response = requests.get(url, params)

    print(response)

    data = response.json
    context = {
        "key": key,
    }
    return render(request, "youtube/servercalll.html")