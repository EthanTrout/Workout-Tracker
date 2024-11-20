from django.http import HttpResponse

from .models import Plan
from profiles.models import UserProfile
from django.contrib.auth.models import User

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        intent = event.data.object
        pid = intent.id
        plan_id = intent.metadata.plan_id
        user_id = intent.metadata.user_id
        # Find the user by username
        user = User.objects.get(id=user_id)

        # Find the UserProfile for the user
        user_profile = UserProfile.objects.get(user=user)

        # Find the plan
        plan = Plan.objects.get(id=plan_id)

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details # updated
        order_total = round(stripe_charge.amount / 100, 2) # updated

         # Clean data in the shipping details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None
        
        order_exists = False
        try:
            order = Order.objects.get(
                email__iexact=billing_details.email,
                phone_number__iexact=billing_details.phone
            )
            plan = order.plan
            user = order.user

            order_exists = True

            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    plan = plan,
                    user = user_profile
                )
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} Error {e}',status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)