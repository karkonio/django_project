from django.contrib import admin
from django.utils.html import format_html

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(
            '<img src="{}" width="300" height="300" />'.format(obj.image.url)
        )

    image_tag.short_description = 'Image'
    list_display = ['user', 'image_tag', 'description']


admin.site.register(Image, ImageAdmin)
