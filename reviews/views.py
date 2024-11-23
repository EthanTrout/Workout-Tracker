from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
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
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    user_profile = get_object_or_404(UserProfile, user=request.user)
    workout = get_object_or_404(Workouts, id=workout_id)

    review = Reviews.objects.create(
        user=user_profile,
        workout=workout,
        description=description,
        rating=rating,
    )

    return JsonResponse({'message': 'Review created successfully'}, status=201)
        