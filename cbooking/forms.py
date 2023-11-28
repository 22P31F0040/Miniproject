from django import forms
from .models import Booking

class Bookhere(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['tracking_number','sender_name','sender_number','receiver_name','receiver_number','status']