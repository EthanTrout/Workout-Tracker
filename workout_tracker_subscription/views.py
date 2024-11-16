from django.shortcuts import render

# Create your views here.

def workout_tracker_subscription(request):
    """ View to return Subscription Page """

    context ={
        
    }
    return render(request,'workout_tracker_subscription/workout_tracker_subscription.html',context)
