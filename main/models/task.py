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
    mod_date = models.DateField(null=True)
    deadline = models.DateField(null=True)
    status = models.CharField(
        max_length=255, default=Status.NEW_TASK, choices=Status.choices, null=True
    )
    priority = models.IntegerField(null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author", null=True
    )
    executor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="executor"
    )

    def __str__(self):
        return self.title
