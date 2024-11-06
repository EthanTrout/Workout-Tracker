# Generated by Django 3.2.25 on 2024-11-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_workoutexercise_week_descriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutexercise',
            name='week_descriptions',
        ),
        migrations.AddField(
            model_name='workout',
            name='week_descriptions',
            field=models.JSONField(default=dict),
        ),
    ]