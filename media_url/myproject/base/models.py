from django.db import models

# Create your models here.
class StudentModel(models.Model):
    std_name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    image = models.ImageField(upload_to='uploads/',default='naruto.jpg')