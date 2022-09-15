from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import product
from accounts.models import Customeuser
from .forms import profile_form

def home(request):
    lastproduct=product.objects.all().order_by('-date_time_create')[0:9]
    return render(request,'pages/home.html',context={'lastproduct':lastproduct})

class Listproduct(generic.ListView):
    model=product
    paginate_by=6
    template_name='pages/list_product.html'
    context_object_name='list_product'

class detailproduct(generic.DetailView):
    model=product
    template_name='pages/detailproduct.html'
    context_object_name='detail_product'

class createproduct(generic.CreateView):
    model=product
    fields=['title','desciption','price','cover','exist','material','place_to_use','weight','date_time_create']
    template_name='pages/create_product.html'
    success_url=reverse_lazy('home_product')

class updateproduct(generic.UpdateView):
    model=product
    template_name='pages/update_product.html'
    fields=['title','desciption','price','cover','exist','material','place_to_use','weight','date_time_create']
    context_object_name='product'
    success_url=reverse_lazy('home_product')

class deleteproduct(generic.DeleteView):
    model=product
    template_name='pages/delete_product.html'
    context_object_name='delete_product'
    success_url=reverse_lazy('home_product')

class profile(LoginRequiredMixin,generic.UpdateView):
    model=Customeuser
    template_name='pages/profile.html'
    form_class=profile_form
    success_url=reverse_lazy('home_product')
    def get_object(self):
        return get_object_or_404(Customeuser,pk=self.request.user.pk)
    def get_form_kwargs(self):
        kwargs=super(profile,self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs

class admin_panel(generic.ListView):
    model=product
    template_name='pages/admin_dashbord.html'
    context_object_name='products'