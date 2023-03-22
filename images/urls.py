from django.urls import path
from . import views

app_name = 'images'
urlpatterns = [
                 path('add_watermark', views.add_watermark, name='add_watermark'),
]