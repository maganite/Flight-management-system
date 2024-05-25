import json
import random

from django.views import generic
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.utils.utils import SideBarSelectedMixin
from apps.map.utils.utils import get_current_path_data
from apps.flight.models import Flight, FlightSensorData, FlightSchedule


class FilghtMapView(LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView):
    template_name = "pages/map/flight_map.html"
    parent = "map"
    segment = "flight_map"


class WeatherConditionsAPI(View):
    def get(self, request):
        # Expanded mock data representing weather conditions across different locations
        data = [
            {"id": 1, "lat": 40.7128, "lon": -74.0060, "radius": 500000, "condition": "sunny", "severity": "low"},
            {"id": 1, "lat": 40.7128, "lon": -74.0060, "radius": 500000, "condition": "thunderstorm", "severity": "low"},
            {"id": 2, "lat": 34.0522, "lon": -118.2437, "radius": 500000, "condition": "sunny", "severity": "low"},
            {"id": 3, "lat": 37.87459, "lon": -94.703125, "radius": 200000, "condition": "High winds", "severity": "high"},
            {"id": 3, "lat": 33.46753, "lon": -101.51367, "radius": 100000, "condition": "Heavy Fog", "severity": "high"},
            {"id": 3, "lat": 37.7749, "lon": -122.4194, "radius": 400000, "condition": "heavy rain", "severity": "high"},
            {"id": 4, "lat": 51.5074, "lon": -0.1278, "radius": 500000, "condition": "snow", "severity": "low"},
            {"id": 5, "lat": 48.8566, "lon": 2.3522, "radius": 400000, "condition": "heavy fog", "severity": "high"},
            {"id": 5, "lat": 48.8566, "lon": 2.3522, "radius": 400000, "condition": "heavy fog", "severity": "high"},
            {"id": 6, "lat": 35.6895, "lon": 139.6917, "radius": 500000, "condition": "light rain", "severity": "low"},
            {"id": 7, "lat": 55.7558, "lon": 37.6173, "radius": 500000, "condition": "sleet", "severity": "medium"},
            {"id": 8, "lat": -33.8688, "lon": 151.2093, "radius": 400000, "condition": "hail", "severity": "high"},
            {"id": 9, "lat": 19.0760, "lon": 72.8777, "radius": 500000, "condition": "smog", "severity": "medium"},
            {"id": 10, "lat": 31.2304, "lon": 121.4737, "radius": 400000, "condition": "dust storm", "severity": "high"}
        ]
        return JsonResponse(data, safe=False)


class GPSLossAreasAPI(View):
    def get(self, request):
        # Expanded mock data representing areas with GPS signal loss
        data = [
            {"id": 1, "lat": 39.7392, "lon": -104.9903, "radius": 200000, "description": "urban skyscraper interference"},
            {"id": 2, "lat": 37.7749, "lon": -122.4194, "radius": 1500, "description": "geomagnetic disturbance"},
            {"id": 3, "lat": 28.5383, "lon": -81.3792, "radius": 800, "description": "high electronic interference"},
            {"id": 4, "lat": 47.6062, "lon": -122.3321, "radius": 500, "description": "military jamming test"},
            {"id": 5, "lat": 40.7128, "lon": -74.0060, "radius": 1200, "description": "satellite maintenance zone"},
            {"id": 6, "lat": 34.0522, "lon": -118.2437, "radius": 1000, "description": "solar flare impact"},
            {"id": 7, "lat": 51.5074, "lon": -0.1278, "radius": 700, "description": "underground tunnel interference"},
            {"id": 8, "lat": 48.8566, "lon": 2.3522, "radius": 900, "description": "historical urban layout interference"}
        ]
        return JsonResponse(data, safe=False)


class VolcanicAshCloudAPI(View):
    def get(self, request):
        # Expanded mock data representing multiple volcanic ash clouds
        data = [
            {
                "id": 1,
                "name": "Mount Fantasia",
                "points": [
                    {"lat": 38.7767, "lon": 142.4580},
                    {"lat": 38.7988, "lon": 142.5902},
                    {"lat": 38.7301, "lon": 142.5376},
                    {"lat": 38.7219, "lon": 142.4321},
                    {"lat": 38.7688, "lon": 142.4099}
                ],
                "description": "Major ash dispersion from Mount Fantasia"
            },
            {
                "id": 2,
                "name": "Mount Spectra",
                "points": [
                    {"lat": 38.6277, "lon": 142.7456},
                    {"lat": 38.6560, "lon": 142.8440},
                    {"lat": 38.5922, "lon": 142.8123},
                    {"lat": 38.5600, "lon": 142.7310},
                    {"lat": 38.6100, "lon": 142.6900}
                ],
                "description": "Ongoing ash dispersion from Mount Spectra"
            }
        ]
        return JsonResponse(data, safe=False)


class FlightPathsAPI(View):
    def get(self, request):
        data = get_current_path_data()
        return JsonResponse(data, safe=False)
    

class AirportMapView(LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView):
    template_name = "pages/map/test.html"
    parent = "map"
    segment = "airport_map"

class AirportAPI(View):
    def get(self, request):
        # Sample data for well-known airports
        data = [
            {"id": "JFK", "name": "John F. Kennedy International Airport", "lat": 40.6413, "lon": -73.7781},
            {"id": "LAX", "name": "Los Angeles International Airport", "lat": 33.9416, "lon": -118.4085},
            {"id": "ORD", "name": "O'Hare International Airport", "lat": 41.9742, "lon": -87.9073},
            {"id": "LHR", "name": "Heathrow Airport", "lat": 51.4700, "lon": -0.4543},
            {"id": "HND", "name": "Tokyo Haneda Airport", "lat": 35.5494, "lon": 139.7798},
            {"id": "CDG", "name": "Charles de Gaulle Airport", "lat": 49.0097, "lon": 2.5479}
        ]
        return JsonResponse(data, safe=False)

class SingleFlightMapView(LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView):
    template_name = "pages/map/single_flight_map.html"
    parent = "map"
    segment = "airport_map"


class GetCurrentFlightData(LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView):
    def get(self, request, **kwargs):
        id = kwargs.get("id")
        try:
            fsd = FlightSensorData.objects.get(flight_schedule_id=id)
        except FlightSensorData.DoesNotExist:
            return JsonResponse([], safe=False)
        fsd_json = serialize('json', [fsd])
        fsd_dict = json.loads(fsd_json)[0]['fields']
        print(fsd_dict)
        return JsonResponse(fsd_dict, safe=False)
