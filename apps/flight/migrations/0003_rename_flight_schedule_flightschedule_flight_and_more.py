# Generated by Django 4.2.13 on 2024-05-25 04:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("flight", "0002_remove_flightschedule_flight_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="flightschedule",
            old_name="flight_schedule",
            new_name="flight",
        ),
        migrations.RenameField(
            model_name="flightsensordata",
            old_name="flight",
            new_name="flight_schedule",
        ),
    ]
