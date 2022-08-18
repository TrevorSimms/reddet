from unicodedata import name
from django.db import models

class Sandbox(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
