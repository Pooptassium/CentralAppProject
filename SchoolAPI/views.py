from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, "schoolapi/home.html")

def servercall(request):
    
    url = "https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/Schools/FeatureServer/0/query?where=1%3D1&objectIds=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=*&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&collation=&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnTrueCurves=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token="


    response = requests.get(url, verify = False)

    data = response.json()

    print(data)

    schools = []

    for record in data["features"]:
        schools.append([
            record["attributes"]["school_name"],
            record["attributes"]["grade_level"]
        ])

    context = {
        "schools" : schools
    }

    return render(request, "schoolapi/servercall.html", context)

def clientcall(request):
    return render(request, "schoolapi/clientcall.hhtml")