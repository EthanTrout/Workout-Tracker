from django.contrib import admin
from .models import UserProfile
from workouts.models import Workout

# Define an inline admin descriptor for Workout model
class WorkoutInline(admin.TabularInline):
    model = Workout
    fk_name = 'owner'  
    extra = 0  

# Customize the UserProfile admin to include the inline workouts
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [WorkoutInline]
    list_display = ('user',)  

# Register UserProfile with the customized admin
admin.site.register(UserProfile, UserProfileAdmin)
