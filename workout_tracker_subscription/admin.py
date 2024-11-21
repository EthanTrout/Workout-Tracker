from django.contrib import admin
from .models import Plan, Order

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'length_in_days', 'is_one_time_payment')
    list_filter = ('is_one_time_payment',)
    search_fields = ('plan_name',)
    ordering = ('plan_name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'email', 'phone_number', 'country', 'date', 'order_total', 'plan', 'user')
    list_filter = ('date', 'country', 'plan')
    search_fields = ('order_number', 'email', 'phone_number')
    readonly_fields = ('order_number', 'date', 'order_total','stripe_pid')
    ordering = ('-date',)

    fieldsets = (
        (None, {
            'fields': ('order_number', 'date', 'order_total', 'plan', 'user')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone_number', 'country')
        }),
    )
