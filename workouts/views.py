from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages 
from django.db.models import Q
from .models import Workout, Fitness, Sport, Level, WorkoutExercise
from exercises.models import Exercise, Bodypart
from profiles.models import UserProfile
from .forms import WorkoutForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


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

            try:
                workouts = workouts.order_by(sort_key)
            except Exception as e:
                messages.error(request,"Cannot sort by this!")
                return redirect(reverse('workouts'))
            
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


def workout_details(request, workout_id):
    """View to show individual workout details"""

    workout = get_object_or_404(Workout, pk=workout_id)
    exercises = workout.exercises.all().order_by('week', 'day')  # Order by week and day
    exercises_by_week_days = {}
    for exercise in exercises:
        if exercise.week not in exercises_by_week_days:
            exercises_by_week_days[exercise.week] = {}  # Create a new dictionary for this week
            
            # Check if the day exists within the week; if not, initialize it
        if exercise.day not in exercises_by_week_days[exercise.week]:
            exercises_by_week_days[exercise.week][exercise.day] = []  # Create a new list for this day

        exercises_by_week_days[exercise.week][exercise.day].append(exercise)

    workout_reviews = workout.workout_reviews.all()
    
    context = {
        'workout': workout,
        'exercises_by_week_days': exercises_by_week_days,
        'workout_reviews':workout_reviews
    }

    return render(request, 'workouts/workout_details.html', context)


@login_required
def save_workout(request, workout_id):
    # Ensure this is a POST request
    if request.method == "POST":
        # Retrieve the workout instance
        workout = get_object_or_404(Workout, id=workout_id)
        
        # Ensure the user is authenticated
        if request.user.is_authenticated:
            # Retrieve or create the user's profile
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            
            # Add the workout to the saved workouts
            user_profile.saved_workouts.add(workout)
            
            messages.success(request, "Workout saved successfully!")
            
            # Get the 'next' parameter for redirection
            redirect_url = request.POST.get('next', 'workouts')  
            return redirect(redirect_url)

        else:
            messages.error(request, "You need to log in to save workouts.")
            return redirect('login')

    # If not a POST request, redirect to workouts
    return redirect('workouts')

def workouts_home(request):
    """View to show individual workout details"""
    levels = Level.objects.all()
    sports = Sport.objects.all()
    fitnesses = Fitness.objects.all()
    
    context = {
        'levels':levels,
        'fitnesses':fitnesses,
        'sports':sports,
    }

    return render(request, 'workouts/workouts_home.html', context)

@login_required
def create_workout(request):
    """Complete workout form and submit"""
    exercises = Exercise.objects.all().order_by('name')
    body_parts = Bodypart.objects.all()
    workout_items = request.session.get('new_workout', {})
    new_workout_exercise = []
    exercises_by_week_days = {} 

    if 'bodypart' in request.GET:
        bodypart_names = request.GET['bodypart'].split(',')
        bodyparts_filter = Bodypart.objects.filter(name__in=bodypart_names)
        if bodyparts_filter.exists():
            # Filter exercises by related bodyparts
            exercises = exercises.filter(
                Q(main_muscles__in=bodyparts_filter)
            ).distinct()  # Avoid duplicates in case an exercise matches multiple filters
        else:
            messages.error(request, "No exercises found for the selected bodypart(s).")

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('create_workout'))
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        exercises = exercises.filter(queries)
    
    workout_form = WorkoutForm(request.POST or None)  # Initialize form only once with request.POST data

    if request.method == "POST" and workout_form.is_valid():
        
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
                
                
            # Initialize the week dictionary if it doesn't exist
                if week not in exercises_by_week_days:
                    exercises_by_week_days[week] = {}  # Create a new dictionary for this week
                
                # Check if the day exists within the week; if not, initialize it
                if day not in exercises_by_week_days[week]:
                    exercises_by_week_days[week][day] = []  # Create a new list for this day

                # Add the exercise data to the correct day and week
                exercises_by_week_days[week][day].append(exercise_data)

        new_workout_instance = workout_form.save()
        week_descriptions ={}
        for week in range(1, 7):
            week_key = f'weekly-desc{week}'  # Form field name
            # Get the description from POST data and strip any whitespace
            description = request.POST.get(week_key, '').strip()

            if description:  # Only add if there's a description
                week_descriptions[week] = description
        
        new_workout_instance.week_descriptions = week_descriptions
        new_workout_instance.owner = request.user.userprofile 
        new_workout_instance.save()  

        for item in new_workout_exercise:
            workout_exercise = WorkoutExercise(
                workout=new_workout_instance,
                exercise=item['exercise'],
                sets=item['sets'],
                reps=item['reps'],
                week=item['week'],
                day=item['day'],
            )
            
            workout_exercise.save()
            
        messages.success(request,f'You have created {new_workout_instance.name} ')
        request.session['new_workout'] = {}
        return redirect(reverse('workout_details',args=[new_workout_instance.id]) + '?created=true')
    

    context = {
        'new_workout': new_workout_exercise,
        'workout_form': workout_form,
        'exercises_by_week_days':exercises_by_week_days,
        'exercises': exercises,
        'body_parts':body_parts
    }

    return render(request, 'workouts/create_workout.html', context)

@login_required
def update_workout_session(request):
    if request.method == "POST":
        # Get the data sent from JavaScript
        data = json.loads(request.body)
        new_workout = data.get('new_workout', {})

        # Save the new workout data in the session
        request.session['new_workout'] = new_workout

        # Optionally, return a success response
        return JsonResponse({"status": "success", "message": "Workout data saved to session"})
    return JsonResponse({"status": "error", "message": "Invalid request"})

@login_required
def reset_workout(request):
    if request.method == "POST":
        try:
            # Your reset logic here, for example:
            # Reset workout data in the session or database
            request.session['new_workout'] = {}

            # Return success response if everything goes well
            return JsonResponse({"success": True})
        except Exception as e:
            # Return error response if something goes wrong
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request method"})

def track_workout_selector(request,workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    saved_workouts = user_profile.saved_workouts.all()
    created_workouts = Workout.objects.filter(owner=user_profile)

    is_saved = workout in saved_workouts
    is_created = workout in created_workouts

    exercises = workout.exercises.all().order_by('week', 'day')  # Order by week and day

    # Initialize counters for weeks and days
    weeks_count = 0
    days_per_week = {}

    for exercise in exercises:
        # Track how many unique weeks
        if exercise.week not in days_per_week:
            weeks_count += 1  # Increment the number of weeks
            days_per_week[exercise.week] = set()  # Use a set to track unique days in the week

        # Track how many unique days in the week
        days_per_week[exercise.week].add(exercise.day)

    # Now, weeks_count will give the total number of unique weeks
    # days_per_week will contain a dictionary with each week and the number of unique days in that week

    week_days_count = {week: len(days) for week, days in days_per_week.items()}

    request.session['week_days_count'] = week_days_count
    request.session['total_weeks'] = weeks_count


    if is_saved or is_created:
        context ={
            'workout':workout,
            'days_per_week':days_per_week
        }
        return render(request,'workouts/track_workout_selector.html',context)
    else:
        messages.error(request,"you do not have this workout saved!")
        return redirect(reverse('workout_details', kwargs={'workout_id': workout_id}))

def track_workout(request,workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    day = int(request.GET.get('day')) 
    week = int(request.GET.get('week')) 
    exercises = workout.exercises.filter(day=day, week=week) 

    week_days_count = request.session.get('week_days_count', {})
    total_weeks = request.session.get('total_weeks', {})
    days_in_week = int(week_days_count.get(str(week), 0))
    
    context={ 
        'exercises': exercises,
        'day': day,
        'days_in_week':days_in_week,
        'workout':workout,
        'week':week
    }
    return render(request,'workouts/track_workout.html',context)


def delete_workout(request,workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if workout.owner != user_profile:
        messages.error(request,"You do not have permission to delete this workout")
    else:
        workout.delete()
    return redirect("profile")

@login_required
def update_workout(request, workout_id):
    """
    View to update an existing workout.
    """
    workout = get_object_or_404(Workout, id=workout_id)
    exercises = workout.exercises.all()  # Use the 'related_name'

    if request.method == "POST":
        workout_form = WorkoutForm(request.POST, instance=workout)
        if workout_form.is_valid():
            workout_form.save()
            messages.success(request, "Workout updated successfully!")
            return redirect('workout_details', workout_id=workout.id)
    else:
        workout_form = WorkoutForm(instance=workout)

    context = {
        'workout': workout,
        'workout_form': workout_form,
        'exercises': exercises,
    }
    return render(request, 'workouts/update_workout.html', context)
