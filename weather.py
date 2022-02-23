"""

"""
import requests
import json


def get_latlong_from_zip(zip_code):
    """
    Gets a latitude and longitude from a zip code.
    This gets its information from the following API: https://www.zippopotam.us/
    """
    zippopotamus_link = 'https://api.zippopotam.us/us/' + zip_code

    request = requests.get(zippopotamus_link)

    request_json = request.json()

    latitude = request_json['places'][0]['latitude']
    longitude = request_json['places'][0]['longitude']

    latlong = (latitude, longitude)

    return latlong


def get_weather_report_from_latlong(latlong):
    """
    Gets a weather report from an input latitude and longitude tuple
    Gets its information for the US Weather Service: https://www.weather.gov/documentation/services-web-api
    """
    grid_api_link = 'https://api.weather.gov/points/' + latlong[0] + ',' + latlong[1]

    grid_request = requests.get(grid_api_link).json()

    forecast_api_link = grid_request["properties"]["forecast"]

    print(forecast_api_link)

    forecast_request = requests.get(forecast_api_link)

    forecast_request_json = forecast_request.json()

    detailed_forecast_afternoon = "This afternoon: " + forecast_request_json["properties"]["periods"][0]["detailedForecast"]
    detailed_forecast_evening = "This evening: " + forecast_request_json["properties"]["periods"][1]["detailedForecast"]

    combined_forecasts = detailed_forecast_afternoon
    return (detailed_forecast_afternoon, detailed_forecast_evening)

def weather():
    latlong = get_latlong_from_zip('97304')
    get_weather_report_from_latlong(latlong)


if __name__ == '__main__':
    weather()