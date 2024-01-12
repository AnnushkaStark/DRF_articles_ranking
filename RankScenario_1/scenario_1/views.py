from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer
from rest_framework.filters import OrderingFilter

# Create your views here.


class ArticleRankApiView(generics.ListAPIView):
    """
    Представление отображения статей
    по ранжированию
    """

    serializer_class = ArticleSerializer

    def get_queryset(self):
        articles = Article.objects.all()
        for article in articles:
            likes = article.likes
            comments = article.comments
            views = article.views
            article.rank = (0.4 * likes) + (0.3 * comments) + (0.2 * views)
        ranked_artickles = sorted(articles, key=lambda x: x.rank, reverse=True)
        return ranked_artickles


class ArticleTimeApiView(generics.ListCreateAPIView):
    """
    Представление отображения статей
    по хронологии
    """

    queryset = Article.objects.all().order_by("-date_create")  # выыбираем все статьи
    serializer_class = ArticleSerializer  # По сериайлайзеру Хронологии
    ordering = ["date_create"]
