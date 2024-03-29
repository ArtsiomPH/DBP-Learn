# Generated by Django 4.1.7 on 2023-03-06 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.PositiveIntegerField(
                        primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("title", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("developer", "Developer"),
                    ("manager", "Manager"),
                    ("admin", "Admin"),
                ],
                default="developer",
                max_length=255,
            ),
        ),
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("creation_date", models.DateField(default=django.utils.timezone.now)),
                ("mod_date", models.DateField()),
                ("deadline", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new_task", "New Task"),
                            ("in_development", "In Development"),
                            ("in_qa", "In Qa"),
                            ("in_code_review", "In Code Review"),
                            ("ready_for_release", "Ready For Release"),
                            ("released", "Released"),
                            ("archived", "Archived"),
                        ],
                        default="new_task",
                        max_length=255,
                    ),
                ),
                ("priority", models.IntegerField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "executor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="executor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
