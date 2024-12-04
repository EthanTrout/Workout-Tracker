from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Reviews
from profiles.models import UserProfile
from workouts.models import Workout

# Create your views here.
@login_required
@require_POST
def create_review(request):
    description = request.POST.get('description')
    rating = request.POST.get('rating')
    workout_id = request.POST.get('workout_id')

    if not description or not rating or not workout_id:
        messages.error(request," Review not submitted :Missing required fields")
        return redirect(reverse('workout_details', args=[workout_id]) )

    user_profile = get_object_or_404(UserProfile, user=request.user)
    workout = get_object_or_404(Workout, id=workout_id)

    review = Reviews.objects.create(
        user=user_profile,
        workout=workout,
        description=description,
        rating=rating,
    )
    messages.success(request,"New review created")
    return redirect(reverse('workout_details', args=[workout_id]) )
        