from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_get_weather_known_city():
    resp = client.get("/weather/London")
    assert resp.status_code == 200
    body = resp.json()
    assert body["city"] == "London"
    assert "temperature_c" in body
    assert "humidity_pct" in body
    assert "condition" in body


def test_get_weather_case_insensitive():
    resp = client.get("/weather/TOKYO")
    assert resp.status_code == 200
    assert resp.json()["city"] == "Tokyo"


def test_get_random():
    resp = client.get("/random")
    assert resp.status_code == 200
    body = resp.json()
    assert "value" in body
    assert 0.0 <= body["value"] < 1.0


