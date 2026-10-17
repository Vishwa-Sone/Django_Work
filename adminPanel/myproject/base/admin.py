from django.contrib import admin
from .models import StudentModel,EmployeeModel

# Register your models here.
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    model = StudentModel
    list_display = ['id','std_name','course']
    search_fields = ['std_name']
# admin.site.register(StudentModel,StudentAdmin)


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    model = EmployeeModel
    list_display = ['id','ename','sal','age']
    search_fields = ['ename']

# admin.site.register(EmployeeModel,EmployeeAdmin)    
