from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField(default=0)
    is_projector = models.BooleanField(default=False)

class Bookings(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_date = models.DateField(blank=True, null=True)
    commentary = models.TextField(null=True)

    class Meta:
        unique_together = ('room_id', 'booking_date',)
