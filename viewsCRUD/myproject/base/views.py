from django.shortcuts import render,redirect
from .models import CarModel
# Create your views here.
def home(request):
    # data = CarModel.objects.get(id=1)
    data_all = CarModel.objects.all()
    filter = CarModel.objects.filter(price=500)
    
    context = {'data_all':data_all,'filter':filter}
    
    
    return render(request,"home.html",context)


def add(request):
    print(request.method) #This method returns GET method
    print(request.GET) 

    if request.method == 'POST':
        print('If condition')
        print(request.method) #This method returns GET method
        print(request.GET) 
        x = request.POST["name"]
        y = request.POST["color"]
        z = request.POST["price"]
        print(x,y,z)
        
        CarModel.objects.create(
            car_name = x,
            color = y,
            price = z
        )
    
     
    if 'name' in request.GET:
        # print(request.GET)
        # print(request.method)
        a = request.GET["name"]
        b = request.GET["color"]
        c = request.GET["price"]
        
        print(a,b,c)
        
        CarModel.objects.create(
            car_name = a,
            color = b,
            price = c
        )
    
    return render(request,"add.html")


def hdelete(request,pk):
    a = CarModel.objects.get(id=pk)
    a.delete()
    return redirect('home')
    
def update(request,pk):
    data = CarModel.objects.get(id=pk)
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['color']
        c = request.POST['price']
        
        data.car_name = a
        data.color = b
        data.price = c
        data.save()
        return redirect('home')
        
    return render(request,'update.html',{'data':data})
    