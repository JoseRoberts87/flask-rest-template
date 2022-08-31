from src import create_app


def test_get_friends_handler(app):
    res = app.test_client().get('/api/friends/')

    assert res.status_code == 200
    assert res.json == {
        "id": "1",
        "name": "John Doe",
        "status": "active"
    }
    assert res.headers.get("Content-Type") == "application/json"
