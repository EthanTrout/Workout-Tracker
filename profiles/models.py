from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class UserProfile(models.Model):
    """ a user profile for storing created workouts and bought workouts """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_workouts = models.ManyToManyField(
        'workouts.Workout', blank=True, related_name='saved_by'
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update the user profile."""
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # If the profile doesn't exist, create it for existing users
        UserProfile.objects.get_or_create(user=instance)
    instance.userprofile.save()