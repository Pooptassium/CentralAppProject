from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "textanalysis/home.html")

def result(request):
    textInput = request.POST["text"]

    context = {
        "textResult" : textInput
    }

    return render(request, "textanalysis/result.html", context)