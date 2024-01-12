from django.test import TestCase
from .models import Article
from datetime import datetime
from datetime import timezone
from .serializers import ArticleSerializer
from django.urls import reverse


class TestAricleModel(TestCase):
    """
    Тестирование модели статьи
    """

    def setUp(self):
        """
        Метод фикстуры тест  статьи
        """
        self.article = Article.objects.create(
            author="testauthor",
            title="testtitle",
            content="testcontetn",
        )

    def test_article_creation(self):
        """
        Тестирование создания в модели статья объекта
        класса статья
        """
        self.assertTrue(isinstance(self.article, Article))

    def test_model_fields(self):
        """
        Тест содержания корректных данных в полях модели
        """

        self.assertIsInstance(self.article.author, str)
        self.assertIsInstance(self.article.title, str)
        self.assertIsInstance(self.article.content, str)
        self.assertIsInstance(self.article.date_create, datetime)
        self.assertIsInstance(self.article.likes, int)
        self.assertIsInstance(self.article.comments, int)
        self.assertIsInstance(self.article.views, int)


class TestArticleSerializer(TestCase):
    """
    Тестирование сериалайзера
    """

    def setUp(self):
        """
        Метод фикстуры тест  статьи
        """
        self.article = Article.objects.create(
            author="testauthor",
            title="testtitle",
            content="testcontetn",
        )

    def test_article_serializer(self):
        """
        Тестирование корректности данных
        для сериализации
        """

        serializer = ArticleSerializer(instance=self.article)
        self.assertEqual(serializer.data["author"], self.article.author)
        self.assertEqual(serializer.data["title"], self.article.title)
        self.assertEqual(serializer.data["content"], self.article.content)
        self.assertEqual(serializer.data["likes"], 0)
        self.assertEqual(serializer.data["comments"], 0)
        self.assertEqual(serializer.data["views"], 0)


class TestArticleRankApiView(TestCase):
    """
    Тестирование представления ранжирования статей
    по алгориму
    """

    def setUp(self):
        """
        Метод фикстуры тест  статьи
        """
        self.article1 = Article.objects.create(
            author="testauthor",
            title="testtitle",
            content="testcontetn",
            likes=300,
            comments=300,
            views=300,
        )
        self.article2 = Article.objects.create(
            author="testauthor",
            title="testtitle",
            content="testcontetn",
            likes=200,
            comments=200,
            views=200,
        )

        self.article3 = Article.objects.create(
            author="testauthor",
            title="testtitle",
            content="testcontetn",
            likes=100,
            comments=100,
            views=100,
        )

        self.url = reverse("rank")

    def test_rank(self):
        """
        тест доступноси эндпойнта
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_ranked_articles(self):
        """
        Тестирование ранжирования статей по алгоритму
        """
        response = self.client.get(self.url)
        self.assertEqual(response.data[0]["likes"], self.article1.likes)
        self.assertEqual(response.data[0]["comments"], self.article1.comments)
        self.assertEqual(response.data[0]["views"], self.article1.views)
        self.assertEqual(response.data[1]["likes"], self.article2.likes)
        self.assertEqual(response.data[1]["comments"], self.article2.comments)
        self.assertEqual(response.data[1]["views"], self.article2.views)
        self.assertEqual(response.data[2]["likes"], self.article3.likes)
        self.assertEqual(response.data[2]["comments"], self.article3.comments)
        self.assertEqual(response.data[2]["views"], self.article3.views)


class TestArticleTimeApiView(TestCase):
    """
    Тестирование представления ранжирования статей
    по хронологии
    """

    def setUp(self):
        """
        Метод фикстуры тест  статьи
        """
        self.article1 = Article.objects.create(
            author="testauthor",
            title="testtitle",
            content="testcontetn",
            likes=300,
            comments=300,
            views=300,
        )
        self.article2 = Article.objects.create(
            author="testauthor",
            title="testtitle",
            content="testcontetn",
            likes=200,
            comments=200,
            views=200,
        )

        self.article3 = Article.objects.create(
            author="testauthor",
            title="testtitle",
            content="testcontetn",
            likes=100,
            comments=100,
            views=100,
        )

        self.url = reverse("time")

    def test_rank(self):
        """
        тест доступноси эндпойнта
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_ranked_articles(self):
        """
        Тестирование ранжирования статей по хронологии
        """
        response = self.client.get(self.url)
        self.assertEqual(response.data[0]["likes"], self.article3.likes)
        self.assertEqual(response.data[0]["comments"], self.article3.comments)
        self.assertEqual(response.data[0]["views"], self.article3.views)
        self.assertEqual(response.data[1]["likes"], self.article2.likes)
        self.assertEqual(response.data[1]["comments"], self.article2.comments)
        self.assertEqual(response.data[1]["views"], self.article2.views)
        self.assertEqual(response.data[2]["likes"], self.article1.likes)
        self.assertEqual(response.data[2]["comments"], self.article1.comments)
        self.assertEqual(response.data[2]["views"], self.article1.views)
