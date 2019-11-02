from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


def test_login_api(db, data):
    user = data[0]
    token = Token.objects.get(user=user)
    client = APIClient()
    print(client)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
