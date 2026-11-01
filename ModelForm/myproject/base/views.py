from django.shortcuts import render,get_object_or_404,redirect
from .forms import Carforms
from .models import CarModel
# Create your views here.
def home(request):
    data = CarModel.objects.all()
    if request.method == "POST":
        form_data = Carforms(request.POST)
        if form_data.is_valid():
            form_data.save()
           
    form = Carforms()
    context = {'form':form,'data':data}
    return render(request,'home.html',context)


def update(request,pk):
    data = get_object_or_404(CarModel,id=pk)
    form = Carforms(instance=data)
    if request.method == 'POST':
        form_data = Carforms(request.POST,instance=data)# It will compare data from database and https request

        if form_data.is_valid():
            form_data.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request,'update.html',context)