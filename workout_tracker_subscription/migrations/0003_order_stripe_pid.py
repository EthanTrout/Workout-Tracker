# Generated by Django 3.2.25 on 2024-11-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker_subscription', '0002_plan_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]