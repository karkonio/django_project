from rest_framework.test import APIRequestFactory
from django_project.api import Login


# test login with correct credentials
def test_login_post_method_ok(db, data):
    profile, photo_1, photo_2, follow1, follow2, token = data
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
