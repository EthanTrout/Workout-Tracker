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

def view_other_profile(request,user_profile_id):
    user_profile = get_object_or_404(UserProfile,pk= user_profile_id)
    workouts = Workout.objects.filter(owner=user_profile)
    context = {
        'profile':user_profile,
        'workouts':workouts,
    }
    return render(request,'profiles/profile.html',context)