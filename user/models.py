from urllib import request
from django.db import models
from django.utils import timezone


# class User(models.Model):
#     name = models.CharField(max_length=255)
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     created_at = models.DateTimeField(default=timezone.now)
#     avatar = models.ImageField(upload_to="avatar", null=True)

#     def __str__(self):
#         return f"{self.username} - {self.email}"
