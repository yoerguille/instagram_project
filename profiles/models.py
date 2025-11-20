from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    
    profile_img = models.ImageField(
        verbose_name='Foto de Perfil',
        upload_to='profile_pictures/',
        blank=True,
        null=True,
    )

    biografia = models.TextField(
        verbose_name='Biografía',
        max_length=500,
        blank=True,
    )

    birth_date = models.DateField(
        verbose_name='Fecha de cumpleaños',
        blank=True,
        null=True,
    )

    # followers= models.ManyToManyField(
    #     'self',
    #     symmetrical=False,
    #     related_name='following',
    #     through='Follow',
    #     verbose_name='Followers',
    # )

    class Meta:    
        verbose_name = 'Perfiles'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.username