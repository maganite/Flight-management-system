# Generated by Django 4.2.13 on 2024-05-25 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0003_remove_company_no_of_empolyees"),
    ]

    operations = [
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fin", models.CharField(max_length=1024)),
                ("model_name", models.CharField(max_length=1024)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FlightSensorData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("current_gps", models.JSONField(blank=True, default=None, null=True)),
                ("current_temperature", models.FloatField(default=0.0)),
                ("current_humidity", models.FloatField(default=0.0)),
                ("current_speed", models.FloatField(default=0.0)),
                ("current_altitude", models.FloatField(default=0.0)),
                ("metadata", models.JSONField(blank=True, default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "flight",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flight.flight",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FlightSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("source", models.CharField(max_length=2048)),
                ("destination", models.CharField(max_length=2048)),
                ("departure_time", models.DateTimeField()),
                ("arrival_time", models.DateTimeField()),
                ("price", models.IntegerField()),
                ("seats", models.IntegerField()),
                ("passengers", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "flight",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flight.flight",
                    ),
                ),
            ],
        ),
    ]
