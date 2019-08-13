import pytest
from django.contrib.auth.models import User

from django_project.models import Image, Profile


@pytest.fixture
def data():
    user = User.objects.create_user(username='user', password='useruser')
    photo_1 = Image.objects.create(
        user=user, image='asd.jpg', description='ASD'
    )
    photo_2 = Image.objects.create(
        user=user, image='asd2.jpg', description='ASD2'
    )
    profile = Profile.objects.create(
        user=user, age=21, city='Bangkok',
        number='+7 787 654 32 10',
        website='https://www.google.com',
        tags='#love, #peace'
    )
    return photo_1, photo_2, user, profile
