from django.shortcuts import render

# Create your views here.
def home(requets):
    return render(requets,"home.html")