from django.db import models
from django.urls import reverse


# Create your models here.

class PostClass(models.Model):
    post_id = models.IntegerField(primary_key=True)
    Slug = models.CharField(max_length=50)
    Title_post = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    Crop_content = models.CharField(max_length=250)
    Full_content = models.CharField(max_length=50)
    Views_post = models.IntegerField()
    Favorites = models.BooleanField(default=False)
    # Likes = models.SmallIntegerField()
    Rating = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts', kwargs={'post_id': self.pk})


class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
