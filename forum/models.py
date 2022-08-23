from django.db import models
from django.utils import timezone
import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"
