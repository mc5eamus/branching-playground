from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI(title="Weather API", version="1.0.0")

ELEPHANT_FACTS: List[str] = [
    "Elephants are the largest land animals on Earth.",
    "An elephant's trunk has over 40,000 muscles.",
    "Elephants can recognise themselves in a mirror.",
    "A baby elephant can stand within 20 minutes of birth.",
    "Elephants mourn their dead and have been observed returning to the bones of deceased relatives.",
    "The African elephant's ears are shaped roughly like the African continent.",
    "Elephants communicate using infrasound — vibrations below the range of human hearing.",
    "An adult elephant eats up to 300 kg of food per day.",
]

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


@app.get("/elephants", tags=["🐘 Definitely Not Weather"])
def get_elephant_facts():
    """Returns a curated list of elephant facts. Unrelated to weather. No regrets."""
    return {"facts": ELEPHANT_FACTS, "count": len(ELEPHANT_FACTS)}
