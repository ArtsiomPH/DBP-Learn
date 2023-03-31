# Generated by Django 4.1.7 on 2023-03-30 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_alter_user_date_of_birth_alter_user_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="executor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="pending_tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
