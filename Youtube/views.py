from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "youtube/home.html'")

def servercall(request):
    key = request.POST["text"]

    context = {
        "key": key,
    }
    return render(request, "youtube/servercalll.html")