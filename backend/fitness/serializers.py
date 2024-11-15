from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Exercise, Workout, Routine

# serializers for routine, workout, exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["workout", "name", "weight", "reps", "sets", "order"]

class WorkoutSerializer(serializers.ModelSerializer):
    # nested serializer - get all exercises
    exercises = ExerciseSerializer(many=True)
    class Meta:
        model = Workout
        fields = ["routine", "name", "description", "order", "exercises"]

class RoutineSerializer(serializers.ModelSerializer):
    # get all workouts
    workouts = WorkoutSerializer(many=True)
    class Meta:
        model = Routine
        fields = ["user", "name", "description", "split", "creation_date", "workouts"]
