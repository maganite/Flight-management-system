# Generated by Django 4.2.13 on 2024-05-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="no_of_empolyees",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
