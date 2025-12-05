from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import UserProfile

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= User
        fields = [
            'first_name',
            'username',
            'email',
            'password',   
        ]

    def save(self, commit= True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data['password'])
        user.save()

        from profiles.models import UserProfile
        UserProfile.objects.create(user=user)

        return user
    
class LoginForm(forms.Form):
    username= forms.CharField(label='Email')
    password=forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class CreatePostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = [
            'image',
            'caption',  
        ]

class FollowForm(forms.Form):
    profile_pk = forms.IntegerField(widget=forms.HiddenInput())
