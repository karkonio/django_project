def test_social(client):
    response = client.get('/')
    assert response.status_code == 404
