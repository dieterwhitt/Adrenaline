from django.db import models
from django.contrib.auth import get_user_model

myUser = get_user_model()

# Routine: a collection of workouts
class Routine(models.Model):
    user = models.ForeignKey(myUser, on_delete=models.CASCADE)
    # name, description, split
    # future options: rotate weekly, choose days of week
    name = models.CharField(32)
    description = models.CharField(256)
    '''
    split_choices = {
        "ppl": "Push-Pull-Legs",
        "hl": "Higher-Lower",

        "custom": "Custom"
    }
    split = models.CharField(choices=split_choices, 
            max_length=16, default="custom")
            '''
    class Meta:
        unique_together = ("user", "order")

# single workout
class Workout(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    # workout information (name, description, order)
    name = models.CharField(32)
    description = models.CharField(256)
    order = models.PositiveSmallIntegerField()
    class Meta:
        unique_together = ("routine", "order")

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    # exercise information (excercise id, reps, weight, sets, order)
    name = models.CharField(32) # key in exercise json, or custom name
    weight = models.PositiveSmallIntegerField(null=True) # kg - null means bodyweight
    reps = models.PositiveSmallIntegerField()
    sets = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    class Meta:
        unique_together = ("workout", "order")
