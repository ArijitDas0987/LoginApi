from django.db import models

class UserModel(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    contact=models.BigIntegerField(max_length=10)