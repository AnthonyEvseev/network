from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PostClass, Test
from .serializer import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    # queryset = PostClass.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return PostClass.objects.all()[:3]

        return PostClass.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Test.objects.get(pk=pk)
        return Response({'cats': cats.name})
