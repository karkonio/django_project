from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Post(models.Model):
    user = models.ForeignKey(
        User, related_name='posts',
        on_delete=models.CASCADE
    )
    image = models.ImageField()
    description = models.TextField(blank=True)


class Profile(models.Model):
    user = models.ForeignKey(
        User, related_name='profile',
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    city = models.CharField(max_length=85)
    phone = models.CharField(unique=True, max_length=30)
    website = models.URLField(max_length=250)
