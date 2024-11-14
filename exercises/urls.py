from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_home, name = 'exercises_home'),
    path('view', views.view_exercises, name = 'view_exercises'),
    path('exercise_details/<exercise_id>/', views.exercise_details, name = 'exercise_details'),
    
 
]
