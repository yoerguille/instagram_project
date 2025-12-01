from django.shortcuts import render
from django.views.generic import CreateView, FormView
from .models import Post
from instagram.froms import CreatePostForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    form_class = CreatePostForm
    success_url =reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, "Post creado correctamente")
        return super(PostCreateView, self).form_valid(form)
