from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=300)
    following = models.ManyToManyField(
        'jwt_auth.User',
        related_name = 'followed_by',
        # on_delete = models.CASCADE,
        blank = True
    )