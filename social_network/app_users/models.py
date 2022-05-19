from django.db import models

# Create your models here.

class UserClass(models.Model):
    user_name = models.CharField(max_length=50)
    login = models.CharField()
    password = models.CharField()
    email = models.CharField()