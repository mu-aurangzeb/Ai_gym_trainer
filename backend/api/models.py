from unicodedata import name
from django.db import models

# Create your models here.
   # list =(id,'name','age','gender','weight','height','created_on','username','password')


class User_info (models.Model):
    id = models.AutoField(primary_key=True)
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight= models.PositiveIntegerField()
    height= models.PositiveIntegerField()
    created_on=models.DateTimeField("created on",auto_now_add=True)
    username=models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=8)



    def __str__(self):
        return self.username

