from lxml import html


def test_home(db, client, data):
    response = client.get('/')
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)

    # assert number of posts
    a = response.cssselect('img.media-object')
    assert len(a) == 2

    # assert rendering the username of image owner
    a = response.cssselect('h3.media-heading')
    assert a[0].text == 'User: user'

    # assert description of 1st image
    a = response.cssselect('div.media-body > p')
    assert a[0].text == 'Description: ASD'

    # assert description of 2nd image
    a = response.cssselect('div.media-body > p')
    assert a[1].text == 'Description: ASD2'
