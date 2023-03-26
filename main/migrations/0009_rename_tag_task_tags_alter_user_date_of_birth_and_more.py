# Generated by Django 4.1.7 on 2023-03-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_user_date_of_birth_user_phone"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="tag",
            new_name="tags",
        ),
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(max_length=13, null=True),
        ),
    ]