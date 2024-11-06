from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_workouts, name = 'workouts'),
    path('home/', views.workouts_home, name = 'workouts_home'),
    path('new_workout/', views.new_workout_details, name = 'new_workout_details'),
    path('save_workout/<workout_id>/', views.save_workout, name = 'save_workout'),
    path('<int:workout_id>/', views.workout_details, name = 'workout_details'),
    
]
