from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView
from django.views.generic import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .froms import RegisterForm, LoginForm
from django.contrib import messages
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from posts.models import Post

class Home(TemplateView):
    template_name = 'general/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_posts = Post.objects.all().order_by('created_at')[:5]
        context["all_posts"] = all_posts
        return context
    

class Login(FormView):
    template_name = 'general/login.html'
    form_class= LoginForm

    def form_valid(self, form):
        usuario = form.cleaned_data.get('username')
        contraseña = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=contraseña)
    
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, f"Bienvenido de nuevo {user.username}")
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(self.request, messages.ERROR, f"Usuario o contraseña incorrectas")
            return super(Login, self).form_invalid(form)

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, f"Cerrado sesión correctamente")
    return HttpResponseRedirect(reverse('home'))

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

@method_decorator(login_required, name='dispatch')
class ProfileDetail(DetailView):
    model = UserProfile
    template_name = 'general/profile_detail.html'

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = UserProfile
    template_name = 'general/profile_update.html'
    fields = [
        'profile_img',
        'biografia',
        'birth_date',
    ]
    context_object_name = 'update'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Perfil editado correctamente")
        return super(ProfileUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile_detail', args=[self.object.pk])
