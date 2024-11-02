from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercise
from django.contrib import messages 
from django.db.models import Q

def all_exercises(request):
    exercises = Exercise.objects.all()
    workout_items = request.session.get('new_workout',{})
    new_workout = []

    if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,"you didn't enter any search criteria!")
                return redirect(reverse('workouts'))
            queries =   Q(name__icontains=query) | Q(description__icontains=query)
            exercises = exercises.filter(queries)
    if workout_items.items:
        for workout_id, details in workout_items.items():
            print(workout_id)
            exercise = get_object_or_404(Exercise, pk=workout_id)
            sets = details.get('sets')
            reps = details.get('reps')

            # Append a dictionary with exercise details to the new_workout list
            new_workout.append({
                'exercise': exercise,
                'sets': sets,
                'reps': reps,
            })

    print(new_workout)
    context = {
        'exercises':exercises,
        'new_workout':new_workout
    }
    return render(request,'exercises/exercises.html',context)

# Create your views here.

def add_to_workout(request,exercise_id):
    """ Adds exercise to new workout """
    sets = request.POST.get('sets')
    reps = request.POST.get('reps')
    redirect_url = request.POST.get('redirect_url')
    new_workout = request.session.get('new_workout', {})

    new_workout[exercise_id] = {
        'exercise_id':exercise_id,
        'sets':sets,
        'reps':reps,
    }
    request.session['new_workout'] = new_workout
    return redirect(redirect_url)

