from datetime import datetime

from django_project.models import Profile, Follower


def test_followers(db):
    bob = Profile.objects.create_user(
        username='bob', password='userbob',
        birthday=datetime(2000, 1, 1)
    )  # follows all
    alice = Profile.objects.create_user(
        username='alice', password='useralice',
        birthday=datetime(1990, 1, 1),
        phone='+7 787 654 32 10'
    )  # follows bob
    lola = Profile.objects.create_user(
        username='lola', password='useralola',
        birthday=datetime(1980, 1, 1),
        phone='+7 707 654 32 50'
    )  #follows alice

    bob_alice = Follower.objects.create(follower=bob, following=alice)
    bob_lola = Follower.objects.create(follower=bob, following=lola)

    alice_bob = Follower.objects.create(follower=alice, following=bob)

    lola_alice = Follower.objects.create(follower=lola, following=alice)

    # bob followings and followers
    assert bob.following.all().count() == 2
    assert bob.following.first() == bob_alice
    assert bob.following.all()[1] == bob_lola

    assert bob.followers.all().count() == 1
    assert bob.followers.first() == alice_bob

    # alice followings and followers
    assert alice.following.all().count() == 1
    assert alice.following.first() == alice_bob

    assert alice.followers.all().count() == 2
    assert alice.followers.first() == bob_alice
    assert alice.followers.all()[1] == lola_alice

    # lola followings and followers
    assert lola.following.all().count() == 1
    assert lola.following.first() == lola_alice

    assert lola.followers.all().count() == 1
    assert lola.followers.first() == bob_lola
