# Generated by Django 3.2.25 on 2024-11-21 16:33

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker_subscription', '0003_order_stripe_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
