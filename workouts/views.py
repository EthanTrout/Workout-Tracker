from django.shortcuts import render, get_object_or_404
from .models import Workout

# Create your views here.

def all_workouts(request):
    """ View to show all workouts """

    workouts = Workout.objects.all()

    context = {
        'workouts':workouts
    }

    return render(request,'workouts/workouts.html',context)


def workout_details(request,workout_id):
    """ View to show individual workout details """

    workout = get_object_or_404(Workout,pk = workout_id)

    context = {
        'workout':workout
    }

    return render(request,'workouts/workout_details.html',context)