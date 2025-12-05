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

    followers= models.ManyToManyField(
         'self',
         symmetrical=False,
         related_name='following',
         through='Follow',
         verbose_name='Followers',
     )

    class Meta:    
        verbose_name = 'Perfiles'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.user.username
    
    def follow(self, profile):
        Follow.objects.get_or_create(follower=self, following=profile)
    
class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, verbose_name='¿Quien sigue?', on_delete=models.CASCADE, related_name='follower_set')
    following = models.ForeignKey(UserProfile, verbose_name='¿A quién sigue?', on_delete=models.CASCADE, related_name='following_set')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='¿Desde cuándo lo sigue?')

    class Meta:
       unique_together=('follower', 'following')
       
    def __str__(self):
       return f"{self.follower} follows {self.following}"
    
    class Meta:    
        verbose_name = 'Seguidor'
        verbose_name_plural = 'Seguidores'
   