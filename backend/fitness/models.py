from django.db import models
from django.contrib.auth import get_user_model

myUser = get_user_model()

# Routine: a collection of workouts
class Routine(models.Model):
    creator = models.ForeignKey(myUser, on_delete=models.CASCADE, 
            related_name="routines")
    # name, description, split
    # future options: rotate weekly, choose days of week
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    split_choices = {
        "ppl": "Push-Pull-Legs",
        "hl": "Higher-Lower",

        "custom": "Custom Split"
    }
    split = models.CharField(choices=split_choices, 
            max_length=16, default="custom")
    creation_date = models.DateField()


# single workout
class Workout(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, 
            related_name="workouts")
    # workout information (name, description, order)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    order = models.PositiveSmallIntegerField()
    class Meta:
        unique_together = ("routine", "order")

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, 
            related_name="exercises")
    # exercise information (excercise id, reps, weight, sets, order)
    name = models.CharField(max_length=32) # key in exercise json, or custom name
    weight = models.PositiveSmallIntegerField(null=True) # kg - null means bodyweight
    reps = models.PositiveSmallIntegerField()
    sets = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    class Meta:
        unique_together = ("workout", "order")
