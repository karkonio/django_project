from django.db import models
from django.contrib.auth.models import User

import json


class Image(models.Model):
    user = models.ForeignKey(
        User, related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField()
    description = models.TextField(blank=True)


class Profile(models.Model):
    AQUARIUS = 'Водолей'
    PISCES = 'Рыбы'
    ARIES = 'Овен'
    TAURUS = 'Телец'
    GEMINI = 'Близнецы'
    CANCER = 'Рак'
    LEO = 'Лев'
    VIRGO = 'Дева'
    LIBRA = 'Весы'
    SCORPIO = 'Скорпион'
    SAGITTARIUS = 'Стрелец'
    CAPRICORN = 'Козерог'

    ZODIAC_CHOICES = (
        (AQUARIUS, AQUARIUS),
        (PISCES, PISCES),
        (ARIES, ARIES),
        (TAURUS, TAURUS),
        (GEMINI, GEMINI),
        (CANCER, CANCER),
        (LEO, LEO),
        (VIRGO, VIRGO),
        (LIBRA, LIBRA),
        (SCORPIO, SCORPIO),
        (SAGITTARIUS, SAGITTARIUS),
        (CAPRICORN, CAPRICORN)
    )

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    zodiak = models.CharField(
        max_length=13, choices=ZODIAC_CHOICES, default=AQUARIUS
    )
    city = models.CharField(max_length=85)
    number = models.CharField(unique=True, max_length=30)
    website = models.URLField(max_length=250)
    tags = models.CharField(max_length=150, blank=True)

    def set_tags(self, x):
        self.tags = json.dumps(x)

    def get_tags(self):
        return self.tags.split(',')
