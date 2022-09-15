from django.urls import path
from . import views

urlpatterns = [
    path('about_us',views.about_us_view,name='about_us'),
    path('contact_us',views.contact_us_view.as_view(),name='contact_us'),
]