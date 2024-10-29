from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_workouts, name = 'all_workouts'),
    path('<workout_id>', views.workout_details, name = 'workout_details'),
    
]
