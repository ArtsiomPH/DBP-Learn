# Generated by Django 4.1.7 on 2023-03-09 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_tag_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="task",
            field=models.ManyToManyField(null=True, to="main.task"),
        ),
        migrations.AlterField(
            model_name="task",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
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
                related_name="inprogress_tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
