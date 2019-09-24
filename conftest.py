import pytest
import datetime

from django_project.models import User, Post, Profile


@pytest.fixture
def data():
    user = User.objects.create_user(
        username='user', password='useruser',
        first_name='User', last_name='Userovich',
        birthday=datetime.datetime(1990, 1, 1)
    )
    photo_1 = Post.objects.create(
        user=user, image='asd.jpg', description='ASD'
    )
    photo_2 = Post.objects.create(
        user=user, image='asd2.jpg', description='ASD2'
    )
    profile = Profile.objects.create(
        user=user, city='Bangkok',
        phone='+7 787 654 32 10', website='https://www.google.com'
    )
    return photo_1, photo_2, user, profile
