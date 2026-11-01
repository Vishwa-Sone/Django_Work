from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.



class CustomUser(AbstractUser):  # Add the fields to the user model in database
    phone_no = models.IntegerField()
    gender = models.CharField(max_length=10)
    
    
class AddressModel(models.Model):
    address = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)