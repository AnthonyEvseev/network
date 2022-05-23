from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PostClass, Author
from .serializer import PostSerializer
from .models import PostClass

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = PostClass.objects.all()
    return render(request, 'app_posts/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def show_post(request, post_id):
    post = get_object_or_404(PostClass, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.Title_post,
        'cat_selected': post.Slug,
    }

    return render(request, 'app_posts/post.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class PostViewSet(viewsets.ModelViewSet):
    # queryset = PostClass.objects.all()
    serializer_class = PostSerializer

    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return PostClass.objects.all()[:3]

        return PostClass.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Author.objects.get(pk=pk)
        return Response({'cats': cats.name})
