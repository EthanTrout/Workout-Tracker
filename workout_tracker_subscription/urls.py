from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_tracker_subscription, name = 'workout_tracker_subscription'),
    path('checkout/', views.checkout, name = 'checkout'),
    
]
