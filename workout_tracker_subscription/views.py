from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .forms import OrderForm
from.models import Plan
import stripe
# Create your views here.

def workout_tracker_subscription(request):
    """ View to return Subscription Page """

    context ={
        
    }
    return render(request,'workout_tracker_subscription/workout_tracker_subscription.html',context)

def checkout(request,plan_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    plan = get_object_or_404(Plan, id=plan_id)
    plan_price = plan.price
    stripe_total = round(plan.price * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency= settings.STRIPE_CURRENCY
        )
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'

    if not stripe_public_key:
        messages.warning(request,"Stripe Public key missing")
    context = {
        'order_form': order_form,
        'plan':plan,
        'stripe_public_key':stripe_public_key,
        'client_secret':intent.client_secret
    }

    return render(request,'workout_tracker_subscription/checkout.html',context)

