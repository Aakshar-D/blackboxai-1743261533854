# Generated by Django 5.1.7 on 2025-03-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RoomBooking",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                (
                    "room_type",
                    models.CharField(
                        choices=[
                            ("single", "Single Room"),
                            ("double", "Double Room"),
                            ("suite", "Suite"),
                        ],
                        max_length=10,
                    ),
                ),
                ("check_in", models.DateField()),
                ("check_out", models.DateField()),
                ("guests", models.IntegerField()),
                ("special_requests", models.TextField(blank=True, null=True)),
                ("booking_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("confirmed", "Confirmed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "ordering": ["-booking_date"],
            },
        ),
    ]
