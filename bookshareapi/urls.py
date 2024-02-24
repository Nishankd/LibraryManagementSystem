from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view())
]

