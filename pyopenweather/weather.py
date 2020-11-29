import asyncio
from requests_async import get
from os import environ
from time import time

class Weather:
    def __init__(self, lat=None, long=None, api_key=None):
        """Class to get weather data from OpenWeatherMap

        Args:
            lat (float, optional): Current latitude. Defaults to None.
            long (float, optional): Current longitude. Defaults to None.
            api_key (string, optional): OpenWeatherMap API Key. Defaults to None.
        """
        self.latitude = lat if lat is not None else environ.get('LATITUDE')
        self.longitude = long if long is not None else environ.get('LONGITUDE')
        self.api_key = api_key if api_key is not None else environ.get('OPENWEATHER_API_KEY')
        self.raw_weather_dict = {}
        self.start_time = time()

    @property
    def latitude(self):
        """Current latitude

        Returns:
            float: Current latitude
        """
        return float(self._latitude)

    @latitude.setter
    def latitude(self, lat):
        self._latitude = lat

    @property
    def longitude(self):
        """Current longitude

        Returns:
            float: Current longitude
        """
        return float(self._longitude)

    @longitude.setter
    def longitude(self, long):
        self._longitude = long

    @property
    def raw_weather_dict(self):
        """Returns a dictionary representation of OpenWeather API JSON data

        The OpenWeather API is rate limited at 60 calls/minute or 1M calls/month
        for the free tier.
        
        https://openweathermap.org/price

        To ensure we do not exceed this limit, we have imposed a cache.

        The API call will only be made on the first call when raw_weather_dict is
        empty, or if at least 10 seconds of time has elapsed since the last time
        the raw_weather_dict property was accessed.

        Returns:
            dict: JSON data from OpenWeather API
        """
        end_time = time()
        time_elapsed = end_time - self.start_time
        if time_elapsed >= 10 or len(self._raw_weather_dict) == 0:
            self._raw_weather_dict = asyncio.run(self.get_current_weather())
            self.start_time = time()
        return self._raw_weather_dict

    @raw_weather_dict.setter
    def raw_weather_dict(self, new_dict):
        self._raw_weather_dict = new_dict

    @property
    def temperature(self):
        """Current temperature in celcius

        Returns:
            float: Current temperature in celcius
        """
        return float(self.raw_weather_dict['main']['temp'])

    @property
    def feels_like(self):
        """Current Human Felt temperature in celcius

        Returns:
            float: Current Human Felt temperature in celcius
        """
        return float(self.raw_weather_dict['main']['feels_like'])

    @property
    def temp_min(self):
        """Minimum observed temperature

        Returns:
            float: Minimum observed temperature
        """
        return float(self.raw_weather_dict['main']['temp_min'])

    @property
    def temp_max(self):
        """Maximum observed temperature

        Returns:
            float: Maximum observed temperature
        """
        return float(self.raw_weather_dict['main']['temp_max'])

    @property
    def pressure(self):
        """Atmospheric pressure in hPa

        Returns:
            int: Atmospheric pressure in hPa
        """
        return int(self.raw_weather_dict['main']['pressure'])

    @property
    def humidity(self):
        """Humidity in %

        Returns:
            int: Humidity in %
        """
        return int(self.raw_weather_dict['main']['humidity'])

    @property
    def visibility(self):
        """Visibility in meters

        Returns:
            int: Visibility in meters
        """
        return int(self.raw_weather_dict['visibility'])

    @property
    def wind_speed(self):
        """Wind speed in meters per second

        Returns:
            float: Wind speed in meters per second
        """
        return float(self.raw_weather_dict['wind']['speed'])

    @property
    def wind_direction(self):
        """Wind direction in degrees

        Returns:
            int: Wind direction in degrees
        """
        return int(self.raw_weather_dict['wind']['deg'])

    async def get_current_weather(self):
        """Returns JSON data of current weather for location

        Examples:
            {
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

        Returns:
            dict: JSON data from OpenWeather API
        """
        query_params = {
          'lat': self.latitude,
          'lon': self.longitude,
          'appid': self.api_key,
          'units': 'metric'
        }
        uri = f'http://api.openweathermap.org/data/2.5/weather'
        request = await get(uri, params=query_params)
        if request.status_code == 200:
          return request.json()
        else:
          print(f'Failed to get current weather. Status code: {request.status_code}')
