from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "textanalysis/home.html")

def counter(request):
    textInput = request.POST["text"]
    return render(request, "textanalysis/result.html", textInput)