from django.db import models
from django.utils.html import format_html
from accounts.models import Customeuser
# Create your models here.

class About_us(models.Model):
    title=models.CharField(max_length=200,verbose_name='title')
    work_description=models.TextField(verbose_name='work_description')
    work_image=models.ImageField(upload_to='work_image',verbose_name='work_image')
    team_member=models.ManyToManyField(Customeuser,verbose_name='team_member')
    def __str__(self):
        return self.title
    def work_image_tag(self):
        return format_html('<img width=150px height=150px src="{}" />'. format(self.work_image.url))
    class Meta:
        verbose_name='Aboutus'

class Contact_us(models.Model):
    subject=models.CharField(max_length=100,verbose_name='subject')
    text=models.TextField(verbose_name='your text')
    author=models.ForeignKey(Customeuser,on_delete=models.CASCADE,verbose_name='author')
    date_time_created=models.DateTimeField(auto_now_add=True,verbose_name='date_time_create')
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name='contactmessage'