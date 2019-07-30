from lxml import html


def test_home(db, client, data):
    response = client.get('/')
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    a = response.cssselect('body > div > ul > div')
    assert len(a) == 2
    b = response.cssselect(
        'body > div > ul > div:nth-child(1) > div > div > div > div > p'
    )
    assert b[0].text == 'ASD'
    b = response.cssselect(
        'body > div > ul > div:nth-child(2) > div > div > div > div > p'
    )
    assert b[0].text == 'ASD2'
