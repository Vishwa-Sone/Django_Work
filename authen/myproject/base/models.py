from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=30)
    id_delete = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    