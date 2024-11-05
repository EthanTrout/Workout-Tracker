from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercise
from django.contrib import messages 
from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse

import uuid

def all_exercises(request):
    exercises = Exercise.objects.all()
    workout_items = request.session.get('new_workout', {})
    new_workout = [] 
    exercises_by_week_days ={}
    last_exercise = None

    # Search functionality
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('workouts'))
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        exercises = exercises.filter(queries)
    
    # Check if workout_items is not empty
    if workout_items:
        for random_id, details in workout_items.items():
            exercise_id = details.get('exercise_id')
            exercise = get_object_or_404(Exercise, pk=exercise_id)
            sets = details.get('sets')
            reps = details.get('reps')
            day =int(details.get('day', 0))
            week =int(details.get('week', 0))
            
            # Append exercise details to new_workout list
            exercise_data = {
                'exercise': exercise,
                'sets': sets,
                'reps': reps,
                'day': day,
                'week':week
            }
            new_workout.append(exercise_data)
            
            # Add to exercises_by_day dictionary
             # Initialize the week dictionary if it doesn't exist
            if week not in exercises_by_week_days:
                exercises_by_week_days[week] = {}  # Create a new dictionary for this week
            
            # Check if the day exists within the week; if not, initialize it
            if day not in exercises_by_week_days[week]:
                exercises_by_week_days[week][day] = []  # Create a new list for this day

            # Add the exercise data to the correct day and week
            exercises_by_week_days[week][day].append(exercise_data)
            
            # Store last exersise to store week and day selected
            last_exercise = exercise_data
            
    if last_exercise is not None:
        selected_day =last_exercise['day']
        selected_week =last_exercise['week']
    else:
        selected_day =1
        selected_week = 1

    # Debugging output
    print(new_workout)
    print(f'Day{selected_day} week:{selected_week}')
    
    # Context data to pass to template
    context = {
        'exercises': exercises,
        'new_workout': new_workout,
        'exercises_by_week_days':exercises_by_week_days,
        'selected_day':selected_day,
        'selected_week':selected_week,

    }
    return render(request, 'exercises/exercises.html', context)


# Create your views here.

def add_to_workout(request,exercise_id):
    """ Adds exercise to new workout """
    sets = request.POST.get('sets')
    reps = request.POST.get('reps')
    day = request.POST.get('day')
    week = request.POST.get('week')
    redirect_url = request.POST.get('redirect_url')
    new_workout = request.session.get('new_workout', {})
    random_id = str(uuid.uuid4())

    if sets == "":
        messages.error(request,"you didn't enter any sets")
        return redirect(reverse('exercises'))
    else:
        new_workout[random_id] = {
            'exercise_id':exercise_id,
            'sets':sets,
            'reps':reps,
            'day':day,
            'week':week
        }
        request.session['new_workout'] = new_workout
        return redirect(redirect_url)


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