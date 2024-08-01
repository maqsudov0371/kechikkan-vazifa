from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=