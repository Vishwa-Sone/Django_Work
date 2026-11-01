from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,"home.html")
    
def student(request,id):
    
    if id == 1:
        return HttpResponse("details of student 1")
    if id == 2:
        return HttpResponse("details of student 2")
    if id == 3:
        return HttpResponse("details of student 3")
    if id == 4:
        return HttpResponse("details of student 4")
    if id == 5:
        return HttpResponse("details of student 5")
        
           
    return HttpResponse("no details")


def employee(request,name):
    if name == 'Kiran':
        return HttpResponse("<h1>Hi i am kiran</h1>")
    
    return HttpResponse("<h1>No details found!!</h1>")