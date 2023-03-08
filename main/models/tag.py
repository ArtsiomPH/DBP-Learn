from django.db import models


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True, null=False, unique=True)
    title = models.CharField(max_length=255)
