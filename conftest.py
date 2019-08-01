import pytest

from django_project.models import Image, User


@pytest.fixture
def data():
    user = User.objects.create_user(username='user', password='useruser')
    photo_1 = Image.objects.create(
        user=user, image='asd.jpg', description='ASD'
    )
    photo_2 = Image.objects.create(
        user=user, image='asd2.jpg', description='ASD2'
    )
    return photo_1, photo_2
