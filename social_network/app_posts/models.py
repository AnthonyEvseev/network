from django.db import models


# Create your models here.

class PostClass(models.Model):
    Post_id = models.IntegerField(primary_key=True)
    Title_post_tr = models.CharField(max_length=50)
    Title_post = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Crop_content = models.CharField(max_length=250)
    Full_content = models.CharField(max_length=50)
    Views_post = models.IntegerField()
    Favorites = models.BooleanField()
    # Likes = models.SmallIntegerField(-1, 0, 1)
    Rating = models.IntegerField()


class Test(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
