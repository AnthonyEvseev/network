from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('<int:Post_id>', categories),
]
