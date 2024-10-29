from django.shortcuts import render
from .models import Workout

# Create your views here.

def all_workouts(request):
    """ View to show all workouts """

    workouts = Workout.objects.all()

    context = {
        'workouts':workouts
    }

    return render(request,'workouts/workouts.html',context)