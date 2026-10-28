from django.http import HttpResponse
from django.shortcuts import render

def apple(request):
    return render(request,"apple.html")

def banana(request):
    return render(request,"banana.html")

def chintu(request):
    return render(request,"chintu.html")

def sheela(request):
    return render(request,"sheela.html")