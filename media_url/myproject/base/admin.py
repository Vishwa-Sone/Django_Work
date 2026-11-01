from django.contrib import admin
from .models import StudentModel

# Register your models here.

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    model = StudentModel
    list_display = ['id','std_name','course','image']
    
    