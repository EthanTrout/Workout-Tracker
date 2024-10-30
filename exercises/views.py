from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercise

def all_exercises(request):
    exercises = Exercise.objects.all()
    workout_items = request.session.get('new_workout',{})
    new_workout = []

    for workout_id in workout_items:
        new_workout.append(get_object_or_404(Exercise,pk=workout_id))

    print(new_workout)
    context = {
        'exercises':exercises,
        'new_workout':new_workout
    }
    return render(request,'exercises/exercises.html',context)

# Create your views here.

def add_to_workout(request):
    """ Adds exercise to new workout """
    exercise_id = int(request.POST.get('exercise_id'))
    redirect_url = request.POST.get('redirect_url')
    new_workout = request.session.get('new_workout', {})

    new_workout[str(exercise_id)] = exercise_id
    request.session['new_workout'] = new_workout
    return redirect(redirect_url)


    
