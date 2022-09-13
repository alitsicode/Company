from django.utils import timezone
from django.db import models
from django.utils.html import format_html

# Create your models here.

class product(models.Model):
    exist=(
        ('have','have'),
        ('in_order','in_order'),
        ('finish','finish'),
    )
    title=models.CharField(max_length=100)
    desciption=models.TextField()
    price=models.BigIntegerField()
    cover=models.ImageField(upload_to='cover')
    exist=models.CharField(max_length=8,choices=exist,default='have')
    material=models.CharField(max_length=50)
    place_to_use=models.CharField(max_length=300)
    weight=models.CharField(max_length=200)
    date_time_create=models.DateTimeField(default=timezone.now())
    def cover_tag(self):
        return format_html('<img width=150px height=150px src="{}" />'. format(self.cover.url))
    actions = ['make_exist','make_order','make_empty']

    
