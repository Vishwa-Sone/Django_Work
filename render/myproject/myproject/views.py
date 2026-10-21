from django.http import HttpResponse
from django.shortcuts import render

def chintu(request):
    return render(request,"chintu.html")
    
def sheela(request):
    return render(request,"sheela.html")

def sona(request):
    return render(request,"sona.html")