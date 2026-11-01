from django.shortcuts import render,redirect
from .models import TodoModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from authen.views import profile_img
from django.db.models import Q
# Create your views here.


@login_required(login_url='login_')
def home(request):
    msg = False
    count = False
    count = TodoModel.objects.filter(user=request.user,id_delete=False).count()

    
    img = profile_img(request)
    if 'q' in request.GET:
        q = request.GET['q']
        data = TodoModel.objects.filter(Q(title__icontains = q) & Q(user = request.user) & Q(id_delete = False) | Q(desc__icontains = q) & Q(user = request.user) & Q(id_delete = False))


        if len(data) == 0:
            messages.error(request,"No record found")
            msg = True
            
    else:
        data = TodoModel.objects.filter(id_delete=False, user=request.user)
    return render(request,'home.html',{'data':data,'img':img,'msg':msg,'count':count})



@login_required(login_url='login_')
def add(request):
    img = profile_img(request)
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        TodoModel.objects.create(
            title = title,
            desc = desc,
            user = request.user
        )
        return redirect('home')
        
    return render(request,'add.html',{'img':img})



@login_required(login_url='login_')
def hdelete(request,pk):
    data = TodoModel.objects.get(id=pk)
    data.id_delete = True
    data.save()
    
    return redirect('trash')


    
@login_required(login_url='login_')   
def trash(request):
    img = profile_img(request)
    data = TodoModel.objects.filter(id_delete = True,user=request.user)
    return render(request,'trash.html',{'data':data,'img':img})


@login_required(login_url='login_')
def restore(request,pk):
    data = TodoModel.objects.get(id=pk)
    data.id_delete = False
    data.save()
    return redirect('home')


@login_required(login_url='login_')
def hdelete_all(request):
    data = TodoModel.objects.filter(user=request.user,id_delete = False)
    for i in data:
        i.id_delete = True
        i.save()
    return redirect('trash')



@login_required(login_url='login_')      
def trestore_all(request):
    data = TodoModel.objects.filter(user=request.user,id_delete = True)
    for i in data:
        i.id_delete = False
        i.save()
    return redirect('home')


@login_required(login_url='login_')
def tdelete(request,pk):
    data = TodoModel.objects.filter(user=request.user,id_delete = True,id=pk)
    data.delete()
    return redirect('trash')


@login_required(login_url='login_')
def tdelete_all(request):
    data = TodoModel.objects.filter(user=request.user,id_delete = True)
    data.delete()
    messages.success(request,"All tasks deleted !!")
    return redirect('trash')