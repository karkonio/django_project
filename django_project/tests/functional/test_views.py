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
    a = response.cssselect(
        'body > div > div:nth-child(2) > div > div > h3 > a'
    )
    assert a[0].text == 'user'

    # assert description of 1st image
    a = response.cssselect('div.media-body > p')
    assert a[0].text == 'Description: ASD'

    # assert description of 2nd image
    a = response.cssselect('div.media-body > p')
    assert a[1].text == 'Description: ASD2'


def test_profile(db, client, data):
    response = client.get('/profile/1/')
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)

    # assert profile users city, phone, website
    a = response.cssselect(
        '#detail > table > tbody > tr:nth-child(3) > td:nth-child(2)'
    )[0]
    assert a.text == 'Bangkok'
    a = response.cssselect(
        '#detail > table > tbody > tr:nth-child(4) > td:nth-child(2)'
    )[0]
    assert a.text == '+7 787 654 32 10'
    a = response.cssselect(
        '#detail > table > tbody > tr:nth-child(5) > td:nth-child(2) > a'
    )[0]
    assert a.text == 'https://www.google.com'
