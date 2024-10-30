from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_exercises, name = 'exercises'),
    path('add_exercise/<exercise_id>/', views.add_to_workout, name = 'add_to_workout'),
 
]
