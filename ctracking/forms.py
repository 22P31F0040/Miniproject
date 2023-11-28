from django import forms
from .models import Tracking

class Trackhere(forms.ModelForm):
    class Meta:
        model=Tracking
        fields=['booking','location']