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


def test_get_weather_unknown_city():
    resp = client.get("/weather/Atlantis")
    assert resp.status_code == 404


def test_get_weather_unknown_city_detail():
    resp = client.get("/weather/Narnia")
    assert resp.status_code == 404
    assert "Narnia" in resp.json()["detail"]


def test_get_weather_all_known_cities():
    cities = ["london", "new york", "tokyo", "paris", "sydney"]
    for city in cities:
        resp = client.get(f"/weather/{city}")
        assert resp.status_code == 200, f"Expected 200 for city '{city}'"


def test_get_weather_response_fields():
    resp = client.get("/weather/paris")
    assert resp.status_code == 200
    body = resp.json()
    assert body["city"] == "Paris"
    assert isinstance(body["temperature_c"], float)
    assert isinstance(body["humidity_pct"], int)
    assert isinstance(body["condition"], str)


def test_get_weather_with_leading_trailing_spaces():
    resp = client.get("/weather/ sydney ")
    assert resp.status_code == 200
    assert resp.json()["city"] == "Sydney"


def test_get_weather_mixed_case():
    resp = client.get("/weather/NeW-YoRk")
    assert resp.status_code == 404


def test_health_response_structure():
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert "status" in body
    assert body["status"] == "ok"
