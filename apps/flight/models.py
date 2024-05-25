from django.db import models

from apps.user.models import Company


class Flight(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    fin = models.CharField(max_length=1024)
    model_name = models.CharField(max_length=1024)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.company} {self.fin}"


class FlightSchedule(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, blank=True, null=True)
    source = models.CharField(max_length=2048)
    destination = models.CharField(max_length=2048)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.IntegerField()
    seats = models.IntegerField()
    passengers = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FlightSensorData(models.Model):
    flight_schedule = models.ForeignKey(FlightSchedule, on_delete=models.CASCADE, blank=True, null=True)
    current_gps = models.JSONField(default=None, null=True, blank=True)
    current_temperature = models.FloatField(default=0.0)
    current_humidity = models.FloatField(default=0.0)
    current_speed = models.FloatField(default=0.0)
    current_altitude = models.FloatField(default=0.0)
    metadata = models.JSONField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
