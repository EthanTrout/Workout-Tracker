from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.workout_tracker_subscription, name = 'workout_tracker_subscription'),
    path('checkout/<int:plan_id>/', views.checkout, name = 'checkout'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('payment_complete/<int:plan_id>/', views.payment_complete, name = 'payment_complete'),
    path('wh/', webhook, name = 'webhook'),

]
