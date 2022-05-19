from django.db import models


# Create your models here.

class PostClass(models.Model):
    Post_id = models.IntegerField()
    Title_post_tr = models.CharField()
    Title_post = models.CharField()
    Author = models.CharField()
    Crop_content = models.CharField(250)
    Full_content = models.CharField()
    Views_post = models.IntegerField()
    Favorites = models.BooleanField()
    Likes = models.SmallIntegerField(-1, 0, 1)
    Rating = models.IntegerField()
