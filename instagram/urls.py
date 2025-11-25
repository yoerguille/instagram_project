from django.urls import include, path
from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import Home, Login, UserRegisterView, Contact, logout_view

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("login/", Login.as_view(), name='login'),
    path("logout/", logout_view, name='logout'),
    path("register/", UserRegisterView.as_view(), name='register'),
    path("contact/", Contact.as_view(), name='contact'),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()
