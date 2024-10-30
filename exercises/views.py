from django.shortcuts import render
from .models import Exercise

def all_exercises(request):
    exercises = Exercise.objects.all()

    context = {
        'exercises':exercises
    }
    return render(request,'exercises/exercises.html',context)

# Create your views here.
