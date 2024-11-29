from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_workouts, name = 'workouts'),
    path('home/', views.workouts_home, name = 'workouts_home'),
    path('create_workout/', views.create_workout, name = 'create_workout'),
    path('save_workout/<workout_id>/', views.save_workout, name = 'save_workout'),
    path('delete_workout/<workout_id>/', views.delete_workout, name = 'delete_workout'),
    path('update_workout/<workout_id>/', views.update_workout, name = 'update_workout'),
    path('<int:workout_id>/', views.workout_details, name = 'workout_details'),
    path('update_workout_session/', views.update_workout_session, name = 'update_workout_session'),
    path('reset_workout/', views.reset_workout, name='reset_workout'),
    path('track_workout_selector/<int:workout_id>/', views.track_workout_selector, name='track_workout_selector'),
    path('track_workout/<workout_id>/', views.track_workout, name='track_workout'),
    
]
