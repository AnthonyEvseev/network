from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:post_id>', show_post, name='posts'),
]
