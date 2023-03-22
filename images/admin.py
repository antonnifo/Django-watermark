from django.contrib import admin
from  .models import Watermark

@admin.register(Watermark)
class WatermarkAdmin(admin.ModelAdmin):
    list_display  = ('name', 'image','added_by', 'date_created')