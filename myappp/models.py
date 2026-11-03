from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name =  models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    summary = models.TextField(max_length=2000)
    previous_work =models.TextField(max_length=2500)
    skills = models.CharField(max_length=500)
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    