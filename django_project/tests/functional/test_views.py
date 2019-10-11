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
        'body > div > div:nth-child(12) > div > div > h3 > a'
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

    # assert profile user birthday
    a = response.cssselect(
        '#detail > table > tbody > tr:nth-child(1) > td:nth-child(2)'
    )[0]
    assert a.text == 'Jan. 1, 1990'

    # assert profile user age
    a = response.cssselect(
        '#detail > table > tbody > tr:nth-child(2) > td:nth-child(2)'
    )[0]
    assert a.text == '29'

    # assert profile user zodiac
    a = response.cssselect(
        '#detail > table > tbody > tr:nth-child(3) > td:nth-child(2)'
    )[0]
    assert a.text == 'Козерог'

    # assert profile user city
    a = response.cssselect(
        '#detail > table > tbody > tr:nth-child(4) > td:nth-child(2)'
    )[0]
    assert a.text == 'Bangkok'

    # assert profile user phone
    a = response.cssselect(
        '#detail > table > tbody > tr:nth-child(5) > td:nth-child(2)'
    )[0]
    assert a.text == '+7 787 654 32 10'

    # assert profile user website
    a = response.cssselect(
        '#detail > table > tbody > tr:nth-child(6) > td:nth-child(2) > a'
    )[0]
    assert a.get('href') == 'https://www.test.com'

    # assert profile followings number
    a = response.cssselect(
        '#myTab > li:nth-child(2) > a'
    )[0]
    assert a.text == 'Подписки: 1'

    # assert profile followers number
    a = response.cssselect(
        '#myTab > li:nth-child(3) > a'
    )[0]
    assert a.text == 'Подписчики: 1'


def test_login_view(db, client, data):
    profile = data[0]
    print(profile)

    # the state of navbar before login
    response = client.get('/')
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    a = response.cssselect(
        '#navbarCollapse > ul > li > a'
    )[0]
    assert a.text == 'Log In'

    # assert fail login process
    response = client.post(
        '/login/', {'username': 'fail', 'password': 'failfail'}
    )
    content = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'  # noqa
    assert content in response.content.decode()

    # assert successful login process
    response = client.post(
        '/login/', {'username': 'user', 'password': 'useruser'}, follow=True
    )
    assert response.status_code == 200
    last_url, status_code = response.redirect_chain[-1]
    assert last_url == '/'

    # the state of navbar after login
    response = client.get('/')
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    a = response.cssselect(
        '#navbarCollapse > ul > li:nth-child(2) > form > \
        input.btn.btn-primary.btn-block.get-started-btn.mt-1.mb-1'
    )[0]
    assert a.value == 'user, Log Out'
