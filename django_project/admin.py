from django.contrib import admin
from django.utils.html import format_html

from .models import User, Post, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_active']


class PostAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(
            '<img src="{}" width="300" height="300" />'.format(obj.image.url)
        )

    image_tag.short_description = 'Image'
    list_display = ['user', 'image_tag', 'description']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birthday', 'city', 'phone', 'website']


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
