from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def home(request):
    data = TodoModel.objects.all()
    return render(request,'home.html',{'data':data})

def about(request):
    return render(request,'about.html')

def complete(request):
    data = CompleteModel.objects.all()
    return render(request,'complete.html',{'data':data})

def trash(request):
    data = TrashModel.objects.all()
    return render(request,'trash.html',{'data':data})


def add(request):
    if request.method == 'POST':
        a = request.POST['text']
        b = request.POST['desc']
        
        TodoModel.objects.create(
            title = a,
            desc = b
        )
        return redirect('home')
        
    return render(request,'add.html')



def hdelete(request,pk):
    data = TodoModel.objects.get(id=pk)
    
    TrashModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('trash')


def update(request,pk):
    data = TodoModel.objects.get(id=pk)
    if request.method == 'POST':
        a = request.POST['title']
        b = request.POST['desc']
        
        data.title = a
        data.desc = b
        data.save()
        return redirect('home')
    
    return render(request,'update.html',{'data':data})


def hcomplete(request,pk):
    data = TodoModel.objects.get(id=pk)
    CompleteModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('complete')

def hcomplete_all(request):
    data = TodoModel.objects.all()
    for i in data:
        CompleteModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('complete')

def hdelete_all(request):
    data = TodoModel.objects.all()
    for i in data:
        TrashModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('trash')
        
        
        
def restore(request,pk):
    data = CompleteModel.objects.get(id=pk)
    TodoModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    
    data.delete()
    return redirect('home')

def cdelete(request,pk):
    data = CompleteModel.objects.get(id=pk)
    TrashModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('trash')
    
def restore_all(request):
    data = CompleteModel.objects.all()
    for i in data:
        TodoModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
        
    return redirect('home')

def cdelete_all(request):
    data = CompleteModel.objects.all()
    for i in data:
        TrashModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
        
    return redirect('trash')

def trestore(request,pk):
    data = TrashModel.objects.get(id=pk)
    TodoModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('home')


def tdelete(request,pk):
    data = TrashModel.objects.get(id=pk)
    data.delete()
    return redirect('trash')


def trestore_all(request):
    data = TrashModel.objects.all()
    for i in data:
        TodoModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('home')


def tdelete_all(request):
    data = TrashModel.objects.all()
    for i in data:
        i.delete()
    return redirect('trash')
    