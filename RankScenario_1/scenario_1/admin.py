from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Регистрация модели статьи
    """

    list_display = (
        "title",
        "author",
        "content",
        "date_create",
        "likes",
        "comments",
        "views",
      
        
    )
