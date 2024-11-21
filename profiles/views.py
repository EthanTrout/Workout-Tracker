from django.shortcuts import render ,get_object_or_404
from .models import UserProfile
from workouts.models import Workout


# Create your views here.



def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    workouts = Workout.objects.filter(owner=request.user.userprofile)
    context = {
        'profile':user_profile,
        'workouts':workouts,
    }
    return render(request,'profiles/profile.html',context)