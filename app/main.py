from fastapi import FastAPI, HTTPException

app = FastAPI(title="Weather API", version="1.0.0")

WEATHER_DATA = {
    "london": {
        "city": "London",
        "temperature_c": 15.0,
        "humidity_pct": 72,
        "condition": "Cloudy",
    },
    "new york": {
        "city": "New York",
        "temperature_c": 22.0,
        "humidity_pct": 58,
        "condition": "Sunny",
    },
    "tokyo": {
        "city": "Tokyo",
        "temperature_c": 28.0,
        "humidity_pct": 80,
        "condition": "Humid",
    },
    "paris": {
        "city": "Paris",
        "temperature_c": 18.0,
        "humidity_pct": 65,
        "condition": "Partly Cloudy",
    },
    "sydney": {
        "city": "Sydney",
        "temperature_c": 12.0,
        "humidity_pct": 55,
        "condition": "Windy",
    },
}


@app.get("/cities")
def get_cities():
    return [data["city"] for data in WEATHER_DATA.values()]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/weather/{city}")
def get_weather(city: str):
    key = city.strip().lower()
    data = WEATHER_DATA.get(key)
    if data is None:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found")
    return data
