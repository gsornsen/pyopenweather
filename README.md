# pyopenweather

pyopenweather is a lightweight asyncronous python wrapper for the [OpenWeatherMap Current Weather Data API](https://openweathermap.org/current)

## Badges

[![Build Status](https://api.travis-ci.com/gsornsen/pyopenweather.svg)](https://travis-ci.com/github/gsornsen/pyopenweather)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cca3c27dfeb541978f507efc06ae0d2e)](https://www.codacy.com/gh/gsornsen/pyopenweather/dashboard)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/cca3c27dfeb541978f507efc06ae0d2e)](https://www.codacy.com/gh/gsornsen/pyopenweather/dashboard)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyopenweather.

```bash
pip install pyopenweather
```

## Usage

### API Key

OpenWeatherMap APIs require an API key to provide valid responses. Please obtain an API key on the [OpenWeatherMap website](https://home.openweathermap.org/users/sign_up).

### Environment Variables

pyopenweather will search for the following environment variables when the `Weather` class is instantiated:

- `OPENWEATHER_API_KEY`
- `LATITUDE`
- `LONGITUDE`

#### API Key

If you set the API key and the environment variable `OPENWEATHER_API_KEY` the library will use it on instantiation, otherwise the API key can be passed in as the `api_key` parameter on instantiation.



### Example

```python
from pyopenweather.weather import Weather


```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
