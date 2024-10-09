from django.urls import path

from . import views

app_name = "newsletter"

urlpatterns = [
    path("home/",views.home,name="home"),
    path("news/",views.news_letter,name="news")
]