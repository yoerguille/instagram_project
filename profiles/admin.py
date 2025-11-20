from django.contrib import admin
from profiles.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    resource_class = UserProfile
    list_dispay= [
        'pk',
        'user',
        'biografia',
        'birth_date',
    ]

