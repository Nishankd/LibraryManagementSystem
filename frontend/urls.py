from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', book_list, name='books'),
    path('detail/<int:pk>/', book_detail, name='detail')
]
