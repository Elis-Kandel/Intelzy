from django.db import models
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  
class Todo(models.Model):
    title=models.CharField(max_length=250)
    completed = models.BooleanField()
    created_at=models.CharField(max_length=250)