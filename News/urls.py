from django.contrib import admin
from django.urls import path, include
from News.views import Index, CreateNews

app_name = 'News'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', CreateNews.as_view(), name='create'),
]
