from django.db import models
from cbooking.models import Booking
# Create your models here.
class Tracking(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking.tracking_number