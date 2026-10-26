from django.shortcuts import render

# Create your views here.
def home(request):
    
    data = "hello im data"
    list = [1,2,3,'abc',[20,30,40]]
    context = {"data":data,"list":list,"age":21}
    return render(request,"home.html",context)


def about(request):
    return render(request,"about.html")