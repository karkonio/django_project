from django.db import models


class Image(models.Model):
    image = models.ImageField()
    description = models.CharField(max_length=120, blank=True, null=True)
