from django.db.models.signals import post_save
from django.dispatch import receiver

from .utils.utils import generate_path
from .models import FlightSensorData


@receiver(post_save, sender=FlightSensorData)
def handle_flight_sensor_data(sender, instance, created, **kwargs):
    if created:
        generate_path(instance, created)
        print(f"New FlightSensorData created for Flight {instance.id} with ID {instance.id}")
    else:
        generate_path(instance, created)
        instance.current_gps
        print(f"FlightSensorData with ID {instance.id} has been updated")
