from django.urls import path, include
from .views import *

urlpatterns = [

    path('', blog),
    path('products', products),
    path('category', category, name='category'),
    path('post', post, name='post'),
]
