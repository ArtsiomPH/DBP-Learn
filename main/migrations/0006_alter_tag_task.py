# Generated by Django 4.1.7 on 2023-03-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_tag_task_alter_task_author_alter_task_executor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="task",
            field=models.ManyToManyField(to="main.task"),
        ),
    ]
