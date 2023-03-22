from django.db import models
from watermarker.models import Watermark
from django.urls import reverse
from django.contrib.auth.models import User

class Watermark(Watermark):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watermarks')

