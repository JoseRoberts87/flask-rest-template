
def test_get_api_handler(app):
    res = app.test_client().get('/api/')

    assert res.status_code == 200
    assert res.json == {
        "message": "this is a sample response from the '/api' endpoint in flask Container",
        "active": False,
    }
    assert res.headers.get("Content-Type") == "application/json"
