from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True, blank=True)

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
    city = models.CharField(max_length=85)
    phone = models.CharField(unique=True, max_length=30)
    website = models.URLField(max_length=250)

    def age(self):
        today = date.today()
        born = self.user.birthday
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))  # noqa
        return age

    def zodiac(self):
        birthday = self.user.birthday
        month = birthday.month
        day = birthday.day
        if (month == 12 and day >= 22) or (month == 1 and day <= 19):
            zodiac = 'Козерог'
        elif (month == 1 and day >= 20) or (month == 2 and day <= 17):
            zodiac = 'Водолей'
        elif (month == 2 and day >= 18) or (month == 3 and day <= 19):
            zodiac = 'Рыбы'
        elif (month == 3 and day >= 20) or (month == 4 and day <= 19):
            zodiac = 'Овен'
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            zodiac = 'Телец'
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            zodiac = 'Близнецы'
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            zodiac = 'Рак'
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            zodiac = 'Лев'
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            zodiac = 'Дева'
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            zodiac = 'Весы'
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            zodiac = 'Скорпион'
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            zodiac = 'Стрелец'
        return zodiac
