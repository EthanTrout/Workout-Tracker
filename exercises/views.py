from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercise, Bodypart
from django.contrib import messages 
from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse

import uuid

# Create your views here.

def view_exercises(request):
    exercises = Exercise.objects.all()

    # Search functionality
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('workouts'))
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        exercises = exercises.filter(queries)

    
    # Context data to pass to template
    context = {
        'exercises': exercises,

    }
    return render(request, 'exercises/view_exercises.html', context)

def exercise_details(request,exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)

    context = {
        'exercise':exercise
    }
    return render(request,'exercises/exercise_details.html',context)

def exercise_home(request):
    
    body_parts = Bodypart.objects.all()

    context = {
        'body_parts':body_parts
    }
    return render(request,'exercises/exercises_home.html',context)
