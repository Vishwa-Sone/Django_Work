from django.db import models

# Create your models here.
class StudentModel(models.Model):
    std_name = models.CharField(max_length=40)
    course = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    
    
class EmployeeModel(models.Model):
    ename = models.CharField(max_length=40)
    sal = models.FloatField(default=0)
    age = models.IntegerField(null=True)
    
    dob = models.DateField(null=True)
    time = models.TimeField(null=True)

    # create_at = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)
    doj = models.DateTimeField(null=True)
    
    
        