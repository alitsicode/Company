from django.contrib import admin
from .models import About_us,Contact_us
# Register your models here.

@admin.register(About_us)
class About_us_Admin(admin.ModelAdmin):
    pass

@admin.register(Contact_us)
class Contact_us_Admin(admin.ModelAdmin):
    list_display=['subject','author','date_time_created']
    ordering=['-date_time_created']
    list_filter=['date_time_created']