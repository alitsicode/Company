from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home_product'),
    path('list/',views.Listproduct.as_view(),name='list_product'),
    path('detail/<int:pk>',views.detailproduct.as_view(),name='detail_product'),
    path('create/',views.createproduct.as_view(),name='create_product'),
    path('update/<int:pk>',views.updateproduct.as_view(),name='update_product'),
    path('delete/<int:pk>',views.deleteproduct.as_view(),name='delete_product'),
    path('profile/',views.profile.as_view(),name='profile'),
    path('admin_panel/',views.admin_panel.as_view(),name='admin_panel'),
]