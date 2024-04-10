from django.db import models

class Payment(models.Model):
    user_id=models.IntegerField(default=None)
    price=models.IntegerField(default=None)
