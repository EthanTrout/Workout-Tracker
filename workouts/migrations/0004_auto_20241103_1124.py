# Generated by Django 3.2.25 on 2024-11-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_workoutexercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutexercise',
            name='day',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='workoutexercise',
            name='week',
            field=models.PositiveIntegerField(default=1),
        ),
    ]