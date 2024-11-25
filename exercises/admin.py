from django.contrib import admin
from django.utils.html import mark_safe  # For rendering HTML in admin
from .models import Exercise, Bodypart

class ExerciseAdmin(admin.ModelAdmin):
    # Display fields in the admin list view
    list_display = ('name', 'image_url_preview', 'description')

    # Add the image preview in the list view based on image_url
    def image_url_preview(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" width="100" height="100" />')  # Show a small image
        return 'No Image URL'

    # Make image_url_preview a column in the admin
    image_url_preview.short_description = 'Image URL Preview'

# Register your models
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Bodypart)
