from django.urls import path
from . import views

app_name = 'images'
urlpatterns = [
    path('add/', views.add_watermark, name='add_watermark'),
    path('upload/', views.watermark_images, name='add_image'),
    path('images/', views.list_images, name='list_images'),
]