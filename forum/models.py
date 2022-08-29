from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, default="Anonymous User")

    def __str__(self):
        return f"{self.title}"
