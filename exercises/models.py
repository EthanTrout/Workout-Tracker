from django.db import models


# Create your models here.

class Bodypart(models.Model):
    name = models.CharField(max_length=254)
    similar_bodyparts = models.ManyToManyField('self', blank=True, symmetrical=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    starting_position = models.TextField(default='')
    execution = models.TextField(default='')
    tips = models.TextField(default='')
    equipment = models.TextField(default='')
    main_muscles = models.ManyToManyField(
        Bodypart, blank=True, related_name='primary_exercises'
    )
    secondary_muscles = models.ManyToManyField(
        Bodypart, blank=True, related_name='secondary_exercises'
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name