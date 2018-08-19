from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


#class Teacher(models.Model):
    #parent_name = models.CharField(max_length=20, null=False, blank=False)
    #relation = models.CharField(max_length=20, null=False, blank=False)
class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    username= models.CharField(max_length=30,null=False,blank=False)
    password = models.CharField(max_length=50,null=False,blank=False)

