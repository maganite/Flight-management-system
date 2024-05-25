from django.urls import path

from .views import (
    ActiveFlightListView,
    InActiveFlightListView,
    CreateFlightView,
    UpdateFlightView,
    GetDataFromSensor
)

app_name = "flight"


urlpatterns = [
    path("active/", ActiveFlightListView.as_view(), name="active_flight_list"),
    path("inactive/", InActiveFlightListView.as_view(), name="inactive_flight_list"),
    path("create/", CreateFlightView.as_view(), name="create_flight"),
    path("edit/<int:id>/", UpdateFlightView.as_view(), name="edit_flight"),
    path("get_data/<int:id>/", GetDataFromSensor.as_view(), name="get_data")
]
