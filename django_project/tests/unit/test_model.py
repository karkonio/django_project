import datetime

from django_project.models import Profile


def test_post_str(db, data):
    profile, photo_1, photo_2, follow1, follow2 = data
    assert str(photo_1) == '1'  # assert first post id
    assert str(photo_2) == '2'  # assert second post id


def test_profile_str(db, data):
    profile = data[0]
    assert str(profile) == 'user'


def test_profile_age(db):
    bday1 = Profile.objects.create_user(
        username='user_1', password='testtest',
        birthday=datetime.datetime(1990, 1, 1)
    )
    assert bday1.age == 29

    bday2 = Profile.objects.create_user(
        username='user_2', password='testtest',
        birthday=datetime.datetime(2000, 2, 28),
        phone='222 22 22'
    )
    assert bday2.age == 19

    bday3 = Profile.objects.create_user(
        username='user_3', password='testtest',
        birthday=datetime.datetime(2004, 12, 31),
        phone='333 33 33'
    )
    assert bday3.age == 14


def test_profile_zodiac(db):
    capricorn = Profile.objects.create_user(
        username='capricorn', password='testtest',
        birthday=datetime.datetime(2019, 12, 22)
    )
    assert capricorn.zodiac == 'Козерог'

    aquarius = Profile.objects.create_user(
        username='aquarius', password='testtest',
        birthday=datetime.datetime(2019, 2, 17), phone='111 11 11'
    )
    assert aquarius.zodiac == 'Водолей'

    pisces = Profile.objects.create_user(
        username='pisces', password='testtest',
        birthday=datetime.datetime(2019, 3, 19), phone='222 22 22'
    )
    assert pisces.zodiac == 'Рыбы'

    aries = Profile.objects.create_user(
        username='aries', password='testtest',
        birthday=datetime.datetime(2019, 3, 20), phone='333 333 33'
    )
    assert aries.zodiac == 'Овен'

    calf = Profile.objects.create_user(
        username='calf', password='testtest',
        birthday=datetime.datetime(2019, 5, 20), phone='444 44 44'
    )
    assert calf.zodiac == 'Телец'

    twins = Profile.objects.create_user(
        username='twins', password='testtest',
        birthday=datetime.datetime(2019, 5, 21), phone='555 55 55'
    )
    assert twins.zodiac == 'Близнецы'

    cancer = Profile.objects.create_user(
        username='cancer', password='testtest',
        birthday=datetime.datetime(2019, 7, 22), phone='666 66 66'
    )
    assert cancer.zodiac == 'Рак'

    leo = Profile.objects.create_user(
        username='leo', password='testtest',
        birthday=datetime.datetime(2019, 7, 23), phone='777 77 77'
    )
    assert leo.zodiac == 'Лев'

    virgo = Profile.objects.create_user(
        username='virgo', password='testtest',
        birthday=datetime.datetime(2019, 9, 22), phone='888 88 88'
    )
    assert virgo.zodiac == 'Дева'

    libra = Profile.objects.create_user(
        username='libra', password='testtest',
        birthday=datetime.datetime(2019, 9, 23), phone='999 99 99'
    )
    assert libra.zodiac == 'Весы'

    scorpio = Profile.objects.create_user(
        username='scorpio', password='testtest',
        birthday=datetime.datetime(2019, 11, 21), phone='000 00 00'
    )
    assert scorpio.zodiac == 'Скорпион'

    sagittarius = Profile.objects.create_user(
        username='sagittarius', password='testtest',
        birthday=datetime.datetime(2019, 11, 22), phone='010 10 10'
    )
    assert sagittarius.zodiac == 'Стрелец'


def test_follower_str(db, data):
    profile, photo_1, photo_2, follow1, follow2 = data
    assert str(follow1) == 'user follows test_user'
    assert str(follow2) == 'test_user follows user'
