from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_exercises, name = 'exercises'),
    path('home', views.exercise_home, name = 'home'),
    path('add_exercise/<exercise_id>/', views.add_to_workout, name = 'add_to_workout'),
    path('view', views.view_exercises, name = 'view_exercises'),
    path('exercise_details/<exercise_id>/', views.exercise_details, name = 'exercise_details'),
    
 
]
