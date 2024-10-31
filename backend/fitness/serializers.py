from rest_framework import serializers
from django.contrib.auth import get_user_model
import models

# serializers for routine, workout, exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercise
        fields = ["workout", "name", "weight", "reps", "sets", "order"]

class WorkoutSerializer(serializers.ModelSerializer):
    # nested serializer - get all exercises
    exercises = ExerciseSerializer(many=True)
    class Meta:
        model = models.Workout
        fields = ["routine", "name", "description", "order"]

class RoutineSerializer(serializers.ModelSerializer):
    # get all workouts
    workouts = WorkoutSerializer(many=True)
    class Meta:
        model = models.Routine
        fields = ["user", "name", "description", "creation_date"]
