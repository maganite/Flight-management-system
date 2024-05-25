from django.urls import path

from apps.map.views import (
    FilghtMapView,
    WeatherConditionsAPI,
    GPSLossAreasAPI,
    VolcanicAshCloudAPI,
    FlightPathsAPI,
    AirportMapView,
    AirportAPI,
    SingleFlightMapView,
    GetCurrentFlightData,
)


app_name = "map"


urlpatterns = [
    path("airports/", AirportMapView.as_view(), name="airport_map"),
    path("single-flight/", SingleFlightMapView.as_view(), name="single_flight_map"),
    path("api/airports/", AirportAPI.as_view(), name="Airport_api"),
    path("flight/", FilghtMapView.as_view(), name="flight_map"),
    path("api/weather/", WeatherConditionsAPI.as_view(), name="weather_conditions_api"),
    path("api/gpsloss/", GPSLossAreasAPI.as_view(), name="gps_loss_areas_api"),
    path("api/volcanic_ash/", VolcanicAshCloudAPI.as_view(), name="volcanic_ash_api"),
    path('api/flight_paths/', FlightPathsAPI.as_view(), name='flight_paths_api'),
    path('api/flight_positions/<int:id>/', GetCurrentFlightData.as_view(), name='get_current_pos'),
]
