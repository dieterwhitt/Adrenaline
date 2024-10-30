from django.db import models

from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.EmailField(unique=True) # set email to be unique
    # additional data (all required fields)
    birthday = models.DateField()
    weight = models.PositiveSmallIntegerField() # weight in kg
    height = models.PositiveSmallIntegerField() # height in cm
    gender_choices = {
        "male": "Male",
        "female": "Female",
        "other": "Other"
    }
    gender = models.CharField(choices=gender_choices, 
            max_length=6, default="other")


