from src import create_app


def test_root_handler():
    app = create_app('TestingConfig')
    res = app.test_client().get('/')

    assert res.status_code == 200
    assert res.json == {'data': 'Hello World!'}
    assert res.headers.get("Content-Type") == "application/json"
