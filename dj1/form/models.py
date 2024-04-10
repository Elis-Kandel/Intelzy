from django.db import models

class User(models.Model):
    username=models.CharField(max_length=250,null=False,blank=False)
    email=models.EmailField( max_length=254,null=False,blank=False)
    gender=models.BooleanField()
