from datetime import date
from dateutil.relativedelta import relativedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel


class Profile(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    city = models.CharField(max_length=85, blank=True)
    phone = models.CharField(unique=True, max_length=30, blank=True)
    website = models.URLField(max_length=250, blank=True)

    @property
    def age(self):
        today = date.today()
        born = self.birthday
        age = relativedelta(today, born).years
        return age

    @property
    def zodiac(self):
        birthday = self.birthday
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

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username


class Post(TimeStampedModel):
    profile = models.ForeignKey(
        Profile, related_name='posts',
        on_delete=models.CASCADE
    )
    image = models.ImageField()
    description = models.TextField(max_length=360, blank=True)

    def __str__(self):
        return str(self.id)


class Follower(models.Model):
    follower = models.ForeignKey(
        Profile, related_name='following',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        Profile, related_name='followers',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return '{} follows {}'.format(self.follower.username, self.following.username)  # noqa
