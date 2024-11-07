from django.shortcuts import render
from exercises.models import Exercise
from itertools import zip_longest
# Create your views here.

def group_list(lst, n):
    """Split a list into chunks of size n."""
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def index(request):
    """ View to return Index Page """

    exercises = Exercise.objects.all()
    grouped_exercises = group_list(exercises, 4)
    context ={
        'exercises':exercises,
        'grouped_exercises':grouped_exercises
    }
    return render(request,'home/index.html',context)

