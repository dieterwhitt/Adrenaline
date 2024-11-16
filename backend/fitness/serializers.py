from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Exercise, Workout, Routine

# serializers for routine, workout, exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "workout", "name", "weight", "reps", "sets", "order"]

class WorkoutSerializer(serializers.ModelSerializer):
    # nested serializer - get all exercises from reverse relationship
    exercises = ExerciseSerializer(many=True, read_only=False)
    class Meta:
        model = Workout
        fields = ["id", "routine", "name", "description", "order", "exercises"]

class RoutineSerializer(serializers.ModelSerializer):
    # get all workouts from reverse relationship (display only)
    workouts = WorkoutSerializer(many=True, read_only=True)
    class Meta:
        model = Routine
        fields = ["id", "creator", "name", "description", "split", "creation_date", "workouts"]
