from django.contrib import admin
from .models import product
from django.contrib import messages
# Register your models here.

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=['title','price','exist','date_time_create','cover_tag']
    ordering=['-date_time_create','exist']
    list_filter=['exist','place_to_use','material']
    search_fields=['title','description']

    actions = ['make_have','make_order','make_empty']

    @admin.action(description='have selected posts')
    def make_have(self,request, queryset):
        queryset.update(exist='have')
        messages.success(request,'your post successfuly exist')
    @admin.action(description='order selected posts')
    def make_order(self,request, queryset):
        queryset.update(exist='in_order')
        messages.success(request,'your post successfuly order')
    @admin.action(description='empty selected posts')
    def make_empty(self,request, queryset):
        queryset.update(exist='empty')
        messages.success(request,'your post successfuly empty')