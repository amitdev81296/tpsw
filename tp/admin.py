from django.contrib import admin
from .models import UserProfile, Post


class UserProfileAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)


admin.site.register(Post, PostAdmin)
