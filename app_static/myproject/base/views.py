from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def mobile(request):
    return render(request,"mobile.html")

def fashion(request):
    return render(request,"fashion.html")