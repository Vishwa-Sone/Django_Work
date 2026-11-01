from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel
# Create your views here.
def home(request):
    form = StudentForm()
    data = StudentModel.objects.all()
    context = {'form':form,'data':data}
    
        # if request.method == "POST":
        #     name = request.POST['name']
        #     number = request.POST['number']
        #     email = request.POST['email']
            
        #     StudentModel.objects.create(
        #         name = name,
        #         phone = number,
        #         email = email
        #     )
            
    if request.method == "POST":
        form_data = StudentForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            
          
    return render(request,'home.html',context)


def update(request,pk):
    data = StudentModel.objects.get(id = pk)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.update(data)
            return redirect('home')
            

    form = StudentForm(initial={
        'name': data.name,
        'number': data.phone,
        'email': data.email
    })

    return render(request, 'update.html', {'form': form})

def form_display(request):
    form = StudentForm()
    context = {'form':form}
    return render(request,'form_display.html',context)