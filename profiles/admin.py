from django.contrib import admin
from profiles.models import UserProfile, Follow
from posts.models import Post, PostComment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    resource_class = UserProfile
    list_dispay= [
        'pk',
        'user',
        'biografia',
        'birth_date',
    ]

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_dispay= [
        "follower",
        'following',
        'created_at',

    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_dispay= [
        "image",
        "caption",
        "created_at",
    ]

@admin.register(PostComment)
class CommentPostwAdmin(admin.ModelAdmin):
    list_dispay= [
        "post",
        "user",
        "text",
        "created_at",
    ]

    
