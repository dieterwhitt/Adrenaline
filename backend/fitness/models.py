from django.db import models
from django.contrib.auth import get_user_model

myUser = get_user_model()

# future model - Split: a collection of workouts (many to many)

class Workout(models.Model):
    user = models.ForeignKey(myUser, on_delete=models.CASCADE)
    # workout information (name, description)
    name = models.CharField(32)
    description = models.CharField(256)

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    # exercise information (excercise id, reps, weight, sets)
    name = models.CharField(32) # key in dict, or custom name
    weight = models.PositiveSmallIntegerField() # kg
    reps = models.PositiveSmallIntegerField()
    sets = models.PositiveSmallIntegerField()
