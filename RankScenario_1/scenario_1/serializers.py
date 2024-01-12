from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    Сериалайзер вывода статей
    по ранжированию
    """

    rank = serializers.FloatField(read_only=True)

    class Meta:
        model = Article
        fields = [
            "author",
            "title",
            "content",
            "date_create",
            "likes",
            "comments",
            "views",
            "rank",
        ]
