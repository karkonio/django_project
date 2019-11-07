from rest_framework.test import APIRequestFactory
from django_project.api import Login, FollowView
from django_project.models import Profile


# test login with correct credentials
def test_login_post_method_ok(db, data):
    profile, photo_1, photo_2, follow1, follow2, token, test_profile = data
    view = Login.as_view()
    factory = APIRequestFactory()
    request = factory.post(
        '/api/auth/',
        {"username": "user", "password": "useruser"},
        format='json'
    )
    response = view(request)
    assert response.status_code == 200
    assert response.data == {'user_id': profile.id, 'token': token.key}


# test login with wrong password
def test_login_post_method_fail(db, data):
    view = Login.as_view()
    factory = APIRequestFactory()
    request = factory.post(
        '/api/auth/',
        {"username": "test_user", "password": "userfuser"},
        format='json'
    )
    response = view(request)
    assert response.status_code == 400
    response.render()
    err_msg = b'{"non_field_errors":["Unable to log in with provided credentials."]}'  # noqa
    assert response.content == err_msg


# test follow process with correct credentials
def test_follow_post_method_ok(db, data):
    profile1 = Profile.objects.create_user(
        username='user1', password='user1user', phone='123'
    )
    profile2 = Profile.objects.create_user(
        username='user2', password='user2user', phone='456'
    )
    assert profile1.id == 3
    assert profile2.id == 4

    view = FollowView.as_view({'post': 'create'})
    factory = APIRequestFactory()
    request = factory.post(
        '/api/follow/', {"current_user_id": 3, "profile_id": 4},
        format='json'
    )
    response = view(request)
    print(response)
    assert response.status_code == 201
    assert response.data == 'follow'
