from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages 
from django.db.models import Q
from .models import Workout, Fitness, Sport, Level, WorkoutExercise
from exercises.models import Exercise
from .forms import WorkoutForm

# Create your views here.

def all_workouts(request):
    """ View to show all workouts """

    workouts = Workout.objects.all()
    query = None
    sports = None
    fitnesses = None
    levels = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'

            workouts = workouts.order_by(sort_key)
            
        if 'fitness' in request.GET:
            fitnesses = request.GET['fitness'].split(',')
            workouts = workouts.filter(fitness__name__in=fitnesses)
            fitnesses = Fitness.objects.filter(name__in=fitnesses)

        if 'sport' in request.GET:
            sports = request.GET['sport'].split(',')
            workouts = workouts.filter(sport__name__in=sports)
            sports = Sport.objects.filter(name__in=sports)

        if 'level' in request.GET:
            levels = request.GET['level'].split(',')
            workouts = workouts.filter(level__name__in=levels)
            levels = Level.objects.filter(name__in=levels)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,"you didn't enter any search criteria!")
                return redirect(reverse('workouts'))
            queries =   Q(name__icontains=query) | Q(fitness__name__icontains=query) | Q(sport__name__icontains=query) | Q(level__name__icontains=query) | Q(description__icontains=query)
            workouts = workouts.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        'workouts':workouts,
        'search_query':query,
        'current_sport':sports,
        'current_fitness':fitnesses,
        'current_level':levels,
        'current_sorting':current_sorting
    }

    return render(request,'workouts/workouts.html',context)


def workout_details(request,workout_id):
    """ View to show individual workout details """

    workout = get_object_or_404(Workout,pk = workout_id)

    context = {
        'workout':workout
    }

    return render(request,'workouts/workout_details.html',context)

def new_workout_details(request):
    """Complete workout form and submit"""
    workout_items = request.session.get('new_workout', {})
    new_workout_exercise = []
    exercises_by_week_days = {} 
    print(workout_items)

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
            new_workout_exercise.append(exercise_data)
            print(new_workout_exercise)
            
           # Initialize the week dictionary if it doesn't exist
            if week not in exercises_by_week_days:
                exercises_by_week_days[week] = {}  # Create a new dictionary for this week
            
            # Check if the day exists within the week; if not, initialize it
            if day not in exercises_by_week_days[week]:
                exercises_by_week_days[week][day] = []  # Create a new list for this day

            # Add the exercise data to the correct day and week
            exercises_by_week_days[week][day].append(exercise_data)

    workout_form = WorkoutForm(request.POST or None)  # Initialize form only once with request.POST data

    if request.method == "POST" and workout_form.is_valid():
        new_workout_instance = workout_form.save()
        for item in new_workout_exercise:
            workout_exercise = WorkoutExercise(
                workout=new_workout_instance,
                exercise=item['exercise'],
                sets=item['sets'],
                reps=item['reps'],
                week=item['week'],
                day=item['day']
            )
            print(workout_exercise)
            workout_exercise.save()
            
        
        
        request.session['new_workout'] = {}
        return redirect(reverse('workouts'))

    context = {
        'new_workout': new_workout_exercise,
        'workout_form': workout_form,
        'exercises_by_week_days':exercises_by_week_days
    }

    return render(request, 'workouts/new_workout_details.html', context)
   