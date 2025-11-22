from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'general/home.html'

class Login(TemplateView):
    template_name = 'general/login.html'

class Register(TemplateView):
    template_name = 'general/register.html'

class Contact(TemplateView):
    template_name = 'general/contact.html'
