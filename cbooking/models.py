from django.db import models

# Create your models here.
class Booking(models.Model):
    tracking_number = models.CharField(max_length=50, unique=True)
    sender_name = models.CharField(max_length=100)
    sender_number=models.IntegerField()
    receiver_name = models.CharField(max_length=100)
    receiver_number=models.IntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.tracking_number
    
