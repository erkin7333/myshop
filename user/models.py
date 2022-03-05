from django.db import models
from django.contrib.auth.models import AbstractUser
from shopcabinet.models import Review



class User(AbstractUser):
    photo = models.ImageField()