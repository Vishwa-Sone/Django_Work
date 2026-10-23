from django.db import models

# Create your models here.
class StudentModel(models.Model):
    std_name = models.CharField(max_length=30)
    course = models.CharField(max_length=40)
    email = models.EmailField(default=100)
    phone_no = models.IntegerField(null=True)
    
    
class employeeModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    gender = models.CharField(null=True)
    sal = models.FloatField(null=True)
    adddress = models.TextField(null=True)
    phone_no = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    dept = models.CharField(null=True)
    
   
    
    
    
    
    
    
    
    
    
    
# python manage.py sqlmigrate base 001 (this use to check how ORM convert model to sql query)