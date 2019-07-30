import pytest

from django_project.models import Image


@pytest.fixture
def data():
    photo_1 = Image.objects.create(image='asd.jpg', description='ASD')
    photo_2 = Image.objects.create(image='asd2.jpg', description='ASD2')
    return photo_1, photo_2
