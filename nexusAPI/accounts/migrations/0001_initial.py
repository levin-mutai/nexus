# Generated by Django 4.2.6 on 2023-10-31 07:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=80, unique=True, verbose_name="email"),
                ),
                ("username", models.CharField(max_length=50, unique=True)),
                ("full_name", models.CharField(max_length=50, unique=True)),
                ("is_email_verified", models.BooleanField(default=False)),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
                (
                    "last_login",
                    models.DateTimeField(auto_now=True, verbose_name="last login"),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
    ]
