from django.urls import include, path
from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import Home, Login, UserRegisterView, Contact, logout_view, ProfileDetail, ProfileUpdate
from django.conf import settings
from django.conf.urls.static import static
from posts.views import PostCreateView

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("login/", Login.as_view(), name='login'),
    path("logout/", logout_view, name='logout'),
    path("register/", UserRegisterView.as_view(), name='register'),
    path("contact/", Contact.as_view(), name='contact'),
    path("profile/<pk>/", ProfileDetail.as_view(), name='profile_detail'),
    path("profile/update/<pk>/", ProfileUpdate.as_view(), name='profile_update'),
    path("post/create/", PostCreateView.as_view(), name='post_create'),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
