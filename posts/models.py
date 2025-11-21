from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.OneToOneField(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to='posts/')

    caption = models.TextField(
        max_length=500,
        blank=True,
        null=True   
    )

    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creacion',
        )
    
    likes = models.ManyToManyField(
        User,
        related_name='liked_posts',
    )

    class Meta:    
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
    
class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:    
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f"Comentó {self.user.username} el post {self.post}"