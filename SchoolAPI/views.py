from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, "schoolapi/home.html")

def servercall(request):
    
    url = "https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/Schools/FeatureServer/0/query?outFields=*&where=1%3D1"

    response = requests.get(url, verify = False)

    data = response.json()

    print(data)

    schools = []

    for record in data["features"]:
        schools.appened([
            record["attributes"]["school_name"],
            record["attributes"]["grade_level"]
        ])

    context = {
        "schools" : schools
    }

    return render(request, "schoolapi/servercall.hhtml", context)

def clientcall(request):
    return render(request, "schoolapi/clientcall.hhtml")