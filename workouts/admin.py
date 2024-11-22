from django.contrib import admin
from .models import Workout, Level, Fitness, Sport, WorkoutExercise

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1  

class WorkoutAdmin(admin.ModelAdmin):
    inlines = [WorkoutExerciseInline]
    list_display = ('id','name', 'description', 'price', 'fitness', 'sport', 'level')  # Adjust fields as needed

# Register models with the customized admin
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Level)
admin.site.register(Fitness)
admin.site.register(Sport)

