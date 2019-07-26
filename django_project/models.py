from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    description = models.CharField(max_length=120)
