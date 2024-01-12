from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    """
    Модель статьи
    """

    author = models.CharField(max_length=50)  # Автор
    title = models.CharField(max_length=100)  # Название
    content = models.TextField(max_length=10000)  # Контент статьи
    date_create = models.DateTimeField(auto_now_add=True)  # Дата создания
    likes = models.IntegerField(default=0)  # Количество лайков
    comments = models.IntegerField(default=0)  # Количество комментариев
    views = models.IntegerField(default=0)  # Количество просмотров

    class Meta:
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f"{self.author} {self.title} {self.content} {self.date_create} {self.likes} {self.comments} {self.views}"
