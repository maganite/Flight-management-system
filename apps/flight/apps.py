from django.apps import AppConfig


class FlightConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.flight"

    def ready(self):
        import apps.flight.signals
