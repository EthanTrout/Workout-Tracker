from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name = 'profile'),
    path('<user_profile_id>/', views.view_other_profile, name = 'view_other_profile'),
    
    
]
