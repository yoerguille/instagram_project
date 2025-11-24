from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .froms import RegisterForm
from django.contrib import messages

class Home(TemplateView):
    template_name = 'general/home.html'

class Login(TemplateView):
    template_name = 'general/login.html'

class UserRegisterView(CreateView):
    model = User
    template_name = 'general/register.html'
    success_url= reverse_lazy('login')
    form_class = RegisterForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente")
        return super().form_valid(form)
    

class Contact(TemplateView):
    template_name = 'general/contact.html'
