
def test_get_main_handler(app):
    res = app.test_client().get('/')

    assert res.status_code == 200
    assert res.json == {'message': 'Hello World!'}
    assert res.headers.get("Content-Type") == "application/json"


def test_post_main_handler(app):
    message = {'message': "My First Awesome API"}
    res = app.test_client().post('/', json=message)

    assert res.status_code == 200
    assert res.json == message
    assert res.headers.get("Content-Type") == "application/json"
