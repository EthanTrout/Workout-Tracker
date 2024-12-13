from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm
from .models import Plan
from profiles.models import UserProfile
import stripe
# Create your views here.

def workout_tracker_subscription(request):
    """ View to return Subscription Page """
    plans = Plan.objects.all()
    context ={
        'plans':plans
    }
    return render(request,'workout_tracker_subscription/workout_tracker_subscription.html',context)

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'plan_id': request.POST.get('plan_id'),
            'user_id': request.user.id,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request,plan_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    plan = get_object_or_404(Plan, id=plan_id)
    plan_price = plan.price
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form_data = {
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            # Add the plan and user to the order
            order.plan = plan
            order.user = user_profile
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()
            return redirect('payment_complete', plan_id)
        else:
            messages.error(request,"There has been an issue with your infomation, Please check them agaian and resubmit")

    else:
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

@login_required
def payment_complete(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'plan':plan,
        'user_profile':user_profile
    }
    return render(request, 'workout_tracker_subscription/payment_complete.html',context)