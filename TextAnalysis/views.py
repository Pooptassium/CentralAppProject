from django.shortcuts import render
from textblob import TextBlob

# Create your views here.
def home(request):
    return render(request, "textanalysis/home.html")

def result(request):
    textInput = request.POST["text"]

    chars = len(textInput)

    words = len(textInput.split(" "))

    blob = TextBlob(textInput)
    sentiment = blob.sentiment

    context = {
        "textResult" : textInput,
        "char_count" : chars,
        "word_count" : words,
        "sentiment" : sentiment
    }

    return render(request, "textanalysis/result.html", context)