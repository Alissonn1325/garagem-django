# Generated by Django 5.0.3 on 2024-03-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_cor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marca",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=50)),
                ("nacionalidade", models.CharField(max_length=50, null=True)),
            ],
        ),
    ]