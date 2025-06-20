# Generated by Django 4.2.21 on 2025-06-05 13:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("title", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=200, unique=True)),
                (
                    "zaragoza_image",
                    cloudinary.models.CloudinaryField(
                        default="placeholder", max_length=255, verbose_name="image"
                    ),
                ),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("about_zaragoza", models.TextField()),
                ("about_me", models.TextField()),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("read", models.BooleanField(default=False)),
            ],
        ),
    ]
