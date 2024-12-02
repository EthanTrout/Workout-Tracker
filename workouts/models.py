from django.db import models
from exercises.models import Exercise
from profiles.models import UserProfile
# Create your models here.

class Fitness(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Sport(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Level(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Workout(models.Model):
    fitness = models.ForeignKey('Fitness', null=True, blank=True, on_delete=models.SET_NULL)
    sport = models.ForeignKey('Sport', null=True, blank=True, on_delete=models.SET_NULL)
    level = models.ForeignKey('Level', null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey('profiles.UserProfile', null=True, blank=True, on_delete=models.SET_NULL, related_name='created_workouts')
    name = models.CharField(max_length=254)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    week_descriptions = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    week = models.PositiveIntegerField(default=1)
    day = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.workout} - {self.exercise} ({self.sets} sets, {self.reps} reps, {self.week} week, {self.day} day)"