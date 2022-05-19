from django.shortcuts import render
from rest_framework import generics
from .models import PostClass
from .serializer import PostSerializer


class PostAPIView(generics.ListCreateAPIView):
    queryset = PostClass.objects.all()
    serializer_class = PostSerializer
