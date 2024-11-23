from django.db import models
from profiles.models import UserProfile
from workouts.models import Workout

# Create your models here.
class Reviews(models.Model):
    user = models.ForeignKey('profiles.UserProfile', null=True,blank=True,on_delete=models.SET_NULL, related_name='user_reviews')
    workout = models.ForeignKey('workouts.Workout',on_delete=models.CASCADE, related_name='workout_reviews')
    description = models.TextField()
    rating = rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)


    def __str__(self):
        f"{self.user.username} - {self.description} "
