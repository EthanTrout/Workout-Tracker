from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from .models import Reviews
from workouts.models import Workout

@receiver(post_save, sender=Reviews)
def update_workout_rating(sender, instance, created, **kwargs):
    """
    Update the overall rating of a workout whenever a review is created or updated.
    """
    
    if instance.rating is not None: 
        workout = instance.workout
        # Calculate the average rating of all reviews for this workout with a non-null rating
        avg_rating = Reviews.objects.filter(workout=workout, rating__isnull=False).aggregate(Avg('rating'))['rating__avg']

        # Update the workout's  rating 
        workout.rating = avg_rating
        workout.save()
