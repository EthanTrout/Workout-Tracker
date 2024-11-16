from django.db import models
import uuid

# Create your models here.
class Plan(models.Model):
    plan_name = models.CharField(max_length=50, null=False, blank=False)
    length_in_days = models.IntegerField(null=True,blank=True)
    is_one_time_payment = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    def __str__(self):
        return self.plan_name

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    plan = models.ForeignKey(Plan, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey('profiles.UserProfile', null=False, blank=False, on_delete=models.CASCADE)

    def _generate_order_number(self):
            """
            Generate a random, unique order number using UUID
            """
            return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        # Calculate order total based on the plan's price
        if self.plan:
            self.order_total = self.plan.price

            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number