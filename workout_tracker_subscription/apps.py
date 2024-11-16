from django.apps import AppConfig


class WorkoutTrackerSubscriptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workout_tracker_subscription'

    def ready(self):
        import workout_tracker_subscription.signals
