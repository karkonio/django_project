from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(
        User, related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)
