from pyopenweather import weather
from unittest.mock import patch, MagicMock

MOCK_JSON_DATA = {
                  "coord": {
                    "lon": -121.89,
                    "lat": 37.34
                  },
                  "weather": [
                    {
                      "id": 800,
                      "main": "Clear",
                      "description": "clear sky",
                      "icon": "01d"
                    }
                  ],
                  "base": "stations",
                  "main": {
                    "temp": 10.9,
                    "feels_like": 8.47,
                    "temp_min": 9,
                    "temp_max": 12.78,
                    "pressure": 1026,
                    "humidity": 49
                  },
                  "visibility": 10000,
                  "wind": {
                    "speed": 0.76,
                    "deg": 341
                  },
                  "clouds": {
                    "all": 1
                  },
                  "dt": 1606589050,
                  "sys": {
                    "type": 1,
                    "id": 5845,
                    "country": "US",
                    "sunrise": 1606575660,
                    "sunset": 1606611055
                  },
                  "timezone": -28800,
                  "id": 5392171,
                  "name": "San Jose",
                  "cod": 200
                }
MOCK_LATITUDE = -121.89
MOCK_LONGITUDE = 37.34
MOCK_API_KEY = f'1234_TOTALLY_REAL_API_KEY_HERE_5678'