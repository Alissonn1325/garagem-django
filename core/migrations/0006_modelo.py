# Generated by Django 5.0.3 on 2024-03-27 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_marca"),
    ]

    operations = [
        migrations.CreateModel(
            name="Modelo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                (
                    "categoria",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Modelo",
                        to="core.categoria",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Modelo",
                        to="core.marca",
                    ),
                ),
            ],
        ),
    ]
