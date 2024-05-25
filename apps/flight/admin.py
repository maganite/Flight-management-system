from django.contrib import admin
from .models import Flight

from .models import Flight, FlightSchedule, FlightSensorData


admin.site.register(Flight)
admin.site.register(FlightSchedule)
admin.site.register(FlightSensorData)
