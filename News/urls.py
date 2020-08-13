from django.contrib import admin
from django.urls import path, include
from News.views import Index

app_name = 'News'
urlpatterns = [
    path('', Index.as_view() , name='index'),
]
