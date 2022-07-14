from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField
    is_projector = models.BooleanField(default=False)
