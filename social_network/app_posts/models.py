from django.db import models
from django.urls import reverse


# Create your models here.

class PostClass(models.Model):
    post_id = models.IntegerField(primary_key=True, verbose_name='Номер записи')
    Slug = models.CharField(max_length=50, verbose_name='Трансит')
    Title_post = models.CharField(max_length=50, verbose_name='Заголовок')
    user_id = models.CharField(max_length=50, verbose_name='Автор')
    Crop_content = models.CharField(max_length=250, verbose_name='Кратко')
    Full_content = models.CharField(max_length=50, verbose_name='Статья')
    Views_post = models.IntegerField(verbose_name='Просмотры')
    Favorites = models.BooleanField(default=False, verbose_name='Избранное')
    Likes = models.SmallIntegerField(null=True, verbose_name='Моя оценка')
    Rating = models.IntegerField(verbose_name="Рейтинг")
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время создания")

    # def __str__(self):
    #     return self.post_id

    def get_absolute_url(self):
        return reverse('posts', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Лента'
        verbose_name_plural = 'Лента'


class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
