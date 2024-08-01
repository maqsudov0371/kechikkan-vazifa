from django.urls import path, include
from .views import *

urlpatterns = [

    path('', home),
    path('products', products),
    path('category', category, name='category'),
    path('post', post, name='post'),
]
