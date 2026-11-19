from app.main import add, app


def test_add():
    assert add(2, 3) == 5


def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_add_route():
    client = app.test_client()
    r = client.get("/add?a=2&b=3")
    assert r.get_json()["result"] == 5
