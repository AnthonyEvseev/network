from django.db import models


# Create your models here.

class UserClass(models.Model):
    user_name = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
