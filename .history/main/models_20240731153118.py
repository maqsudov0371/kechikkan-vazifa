from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField(max_length=13)
    age = models.PositiveIntegerField(defoult=0)

    def __str__(self):
        return self.username
    

class Category()


class Post(models.Model):
    title = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
