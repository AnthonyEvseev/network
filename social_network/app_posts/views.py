from django.shortcuts import render
from rest_framework import generics
from .models import PostClass
from .serializer import PostSerializer


class PostAPIView(generics.ListAPIView):
    queryset = PostClass.object.all()
    serializer_class = PostSerializer
