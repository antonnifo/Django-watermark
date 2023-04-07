from django.urls import path
from . import views

app_name = 'images'
urlpatterns = [
                 path('add/', views.add_watermark, name='add_watermark'),
]