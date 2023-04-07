from django import forms
from .models import Watermark, Image

class WatermarkForm(forms.ModelForm):
    class Meta:
        model = Watermark
        fields = ("name", "image",)

class ImageAddForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("name", "image",)
