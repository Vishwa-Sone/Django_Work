from django.db import models

# Create your models here.
class FruitsModel(models.Model):
    fname = models.CharField(max_length=30)
    price = models.FloatField()
    