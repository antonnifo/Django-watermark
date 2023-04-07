from django.db import models
from watermarker.models import Watermark
from django.urls import reverse
from django.contrib.auth.models import User

class Watermark(Watermark):
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='watermarks')

class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='images')
