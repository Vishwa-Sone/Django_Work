from django.db import models

# Create your models here.
class CarModel(models.Model):
    car = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    price = models.IntegerField()