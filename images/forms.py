from django import forms
from .models import Watermark

class WatermarkForm(forms.ModelForm):
    
    class Meta:
        model = Watermark
        fields = ("name", "image",)
