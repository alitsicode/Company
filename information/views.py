from django.shortcuts import render,redirect,get_object_or_404
from .models import About_us,Contact_us
from django.views import generic
from django.contrib import messages
# Create your views here.

def about_us_view(request):
    about=About_us.objects.last()
    return render(request,'information/about_us.html',context={'about':about})

class contact_us_view(generic.CreateView):
    model=Contact_us
    fields=['subject','text']
    template_name='information/contact_us.html'
    success_url='/'
    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.author=self.request.user
        instance.save()
        messages.success(self.request, "your message successfuly send to us")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About_us.objects.last()
        return context
    