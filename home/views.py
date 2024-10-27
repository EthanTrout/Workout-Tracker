from django.shortcuts import render

# Create your views here.

def index(request):
    """ View to return Index Page """
    return render(request,'home/index.html')