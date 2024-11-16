from django.conf import settings

def one_time_payment(request):
    return {
        'ONE_TIME_PAYMENT': getattr(settings, 'ONE_TIME_PAYMENT', None),
    }

def monthly_payment(request):
    return {
        'MONTHLY_PAYMENT': getattr(settings, 'MONTHLY_PAYMENT', None),
    }