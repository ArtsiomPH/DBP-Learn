from django.db import models
from .task import Task


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True, null=False, unique=True)
    title = models.CharField(max_length=255)
    task = models.ManyToManyField(Task, null=True)

    def __str__(self):
        return self.title
