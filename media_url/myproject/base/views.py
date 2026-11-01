from django.shortcuts import render
from .models import StudentModel


# Create your views here.
def home(request):
    data = StudentModel.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        course = request.POST['course']
        img = request.FILES.get('img')
        StudentModel.objects.create(
            std_name = name,
            course = course,
            image = img if img else 'naruto.jpg'
        )
        

    return render(request, 'home.html',{'data':data})