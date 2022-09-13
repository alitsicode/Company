from django.shortcuts import render,redirect,get_object_or_404
from .models import About_us,Contact_us
# Create your views here.

def about_us_view(request):
    about=About_us.objects.last()
    return render(request,'information/about_us.html',context={'about':about})