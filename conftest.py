import pytest
import datetime

from django_project.models import Profile, Post, Follower


@pytest.fixture
def data():
    profile = Profile.objects.create_user(
        username='user', password='useruser',
        first_name='User', last_name='Userovich',
        birthday=datetime.datetime(1990, 1, 1),
        avatar='ava.jpg', city='Bangkok',
        phone='+7 787 654 32 10', website='https://www.test.com'
    )
    photo_1 = Post.objects.create(
        profile=profile, image='asd.jpg', description='ASD'
    )
    photo_2 = Post.objects.create(
        profile=profile, image='asd2.jpg', description='ASD2'
    )
    test_profile = Profile.objects.create_user(
        username='test_user', password='useruser',
        birthday=datetime.datetime(2000, 1, 1)
    )
    follow1 = Follower.objects.create(follower=profile, following=test_profile)
    follow2 = Follower.objects.create(follower=test_profile, following=profile)

    return profile, photo_1, photo_2, follow1, follow2
