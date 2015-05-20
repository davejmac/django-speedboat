from django.db import models
from django.conf import settings


class Speedboat(models.Model):

    a_field = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
