from django.urls import path
from . views import ArticleRankApiView, ArticleTimeApiView


urlpatterns =[
    path('rank/', ArticleRankApiView.as_view(), name="rank" ),
    path('time/', ArticleTimeApiView.as_view(), name="time")
]