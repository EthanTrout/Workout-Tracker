from django.shortcuts import render
from .forms import OrderForm
# Create your views here.

def workout_tracker_subscription(request):
    """ View to return Subscription Page """

    context ={
        
    }
    return render(request,'workout_tracker_subscription/workout_tracker_subscription.html',context)

def checkout(request):

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_0SMREd7Vdweb1MGRi8S0EycR00JVzSAs5O',
        'client_secret': 'test client secret',
    }

    return render(request,'workout_tracker_subscription/checkout.html',context)