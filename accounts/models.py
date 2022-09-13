from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customeuser(AbstractUser):
    age=models.PositiveIntegerField(null=True,default=0,verbose_name='age')
    is_author=models.BooleanField(default=False,verbose_name='is_author')
    email=models.EmailField(max_length=254,unique=True,verbose_name='email')
    first_name=models.CharField(max_length=200,default='firstname',verbose_name='firstname')
    last_name=models.CharField(max_length=200,default='lastname',verbose_name='lastname')
    avatar=models.FileField(null=True,blank=True,upload_to='user_avatar',verbose_name='avatar')
    class Meta:
        verbose_name='CustomeUser'
