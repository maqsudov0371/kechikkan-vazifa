from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField(max_length=13)
    age