from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def update_user_profile_plan(sender, instance, created, **kwargs):
    """
    Update the UserProfile's plan to match the plan in the Order.
    """
    user_profile = instance.user
    if created or user_profile.plan != instance.plan:
        user_profile.plan = instance.plan
        user_profile.save()
