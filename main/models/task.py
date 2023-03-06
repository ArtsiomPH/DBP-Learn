import django.utils.timezone
from django.db import models

from .user import User


class Task(models.Model):
    class Status(models.TextChoices):
        NEW_TASK = "new_task"
        IN_DEVELOPMENT = "in_development"
        IN_QA = "in_qa"
        IN_CODE_REVIEW = "in_code_review"
        READY_FOR_RELEASE = "ready_for_release"
        RELEASED = "released"
        ARCHIVED = "archived"

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    creation_date = models.DateField(default=django.utils.timezone.now)
    mod_date = models.DateField()
    deadline = models.DateField()
    status = models.CharField(
        max_length=255, default=Status.NEW_TASK, choices=Status.choices
    )
    priority = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    executor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="executor"
    )
