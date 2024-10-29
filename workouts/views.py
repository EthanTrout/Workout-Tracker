from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages 
from django.db.models import Q
from .models import Workout

# Create your views here.

def all_workouts(request):
    """ View to show all workouts """

    workouts = Workout.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,"you didn't enter any search criteria!")
                return redirect(reverse('workouts'))
            queries =   Q(name__icontains=query) | Q(fitness__name__icontains=query) | Q(sport__name__icontains=query) | Q(level__name__icontains=query) | Q(description__icontains=query)
            workouts = workouts.filter(queries)

    context = {
        'workouts':workouts,
        'search_query':query
    }

    return render(request,'workouts/workouts.html',context)


def workout_details(request,workout_id):
    """ View to show individual workout details """

    workout = get_object_or_404(Workout,pk = workout_id)

    context = {
        'workout':workout
    }

    return render(request,'workouts/workout_details.html',context)