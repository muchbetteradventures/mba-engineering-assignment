# Generated by Django 5.1.2 on 2024-12-17 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0003_alter_booking_options"),
        ("companies", "__first__"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="company",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="companies.company",
            ),
            preserve_default=False,
        ),
    ]
