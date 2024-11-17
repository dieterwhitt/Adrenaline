from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from jsonschema import validate, ValidationError
import os
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import Exercise, Workout, Routine
from .serializers import ExerciseSerializer, WorkoutSerializer, RoutineSerializer

# loads fitness/data/muscles.json and validates it, then sends it
@api_view(["GET"])
def get_muscles(request):
    try:
        # open muscles.json and remove invalid entries
        # schema defines muscle object. in json: {"muscle_name" : {muscle_schema}}
        muscle_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "group": {
                    "type": "string",
                    "enum": ["Chest", "Back", "Arms", "Abdominals", "Legs", "Shoulders"]
                },
                "subgroup": {
                    "type": "string",
                    "enum": ["Calves", "Thighs", "Hips", "Waist", "Upper Arms",
                            "Forearms"]
                },
                "male_segments": {
                    "type": "array",
                    "items": {
                        "type" : "integer"
                    }},
                "female_segments": {
                    "type": "array",
                    "items": {
                        "type" : "integer"
                    }}
            },
            "required": ["id", "group", "male_segments", "female_segments"]
        }
        path = os.path.join(os.path.dirname(__file__), "data/muscles.json")
        with open(path, "r") as raw:
            muscles = json.load(raw)
        
        invalid = [] # invalid muscle entries - will be removed from response
        for name in muscles:
            try:
                data = muscles[name]
                validate(instance=data, schema=muscle_schema)
            except ValidationError as ve:
                # issue with muscle data: delete entry from output
                invalid.append((name, ve))
        for pair in invalid:
            del muscles[pair[0]]
            print("INVALID MUSCLE: ", pair[0])
        # send back valid muscles dict
        return Response(muscles, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# loads fitness/data/exercises.json and validates it
@api_view(["GET"])
def get_exercises(request):
    try:
        # in json: {"exercise_name" : {exercise_schema}}
        exercise_schema = {
            "type": "object",
            "properties": {
                "id": {"type" : "integer"},
                # primary and secondary: not enforcing existence in muscles
                "primary": {
                    "type": "array",
                    "items": {
                        "type" : "String"
                    }
                },
                "secondary": {
                    "type": "array",
                    "items": {
                        "type" : "string"
                    }
                },
                "category": {
                    "enum": ["Aerobic", "Anaerobic", "Strength", "Flexibility"]
                }
            },
            "required" : ["id", "primary", "secondary", "category"]
        }
        with open("./data/exercises.json", "r") as raw:
            exercises = json.load(raw)
        invalid = []
        for name in exercises:
            try:
                data = exercises[name]
                validate(instance=data, schema=exercise_schema)
            except ValidationError as ve:
                # issue with exercise data: delete entry from output
                invalid.append((name, ve))
        for pair in invalid:
            del exercises[pair[0]]
            print("INVALID EXERCISE: ", pair[0])
        return Response(exercises, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# instead of apiview: use viewsets for abstract crud monkeying

# tested so far: routines
# future: workouts, exercises
# crud on other users objects

class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # define the list of db rows to include in queryset
    # user matches request user (authenticated)
    def get_queryset(self):
        return Exercise.objects.filter(workout__routine__creator=self.request.user)
    # decorator: return bad request if workout doesn't belong to user
    def validate_exercise(func):
        def wrapper(self, request, *args, **kwargs):
            try:
                workout_id = request.data.get("workout", None)
                workout = Workout.objects.get(pk=workout_id)
                routine = workout.routine
                if routine.creator != request.user:
                    raise ValueError("user does not own this routine")
                return func(self, request, *args, **kwargs)
            except Exception as e:
                return Response({"message": f"associated routine is invalid: {e}"}, 
                        status.HTTP_400_BAD_REQUEST)
        return wrapper

    @validate_exercise
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @validate_exercise
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @validate_exercise
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Workout.objects.filter(routine__creator=self.request.user)
    # decorator: return bad request if routine doesn't belong to user
    # it is still possible (although not ideal) to update a workout to belong
    # to another routine.
    def validate_workout(func):
        def wrapper(self, request, *args, **kwargs):
            try:
                routine_id = request.data.get("routine", None)
                routine = Routine.objects.get(pk=routine_id)
                if routine.creator != request.user:
                    raise ValueError("user does not own this routine")
                return func(self, request, *args, **kwargs)
            except Exception as e:
                return Response({"message": f"associated routine is invalid: {e}"}, 
                        status.HTTP_400_BAD_REQUEST)
        return wrapper

    @validate_workout
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @validate_workout
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @validate_workout
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class RoutineViewSet(viewsets.ModelViewSet):
    serializer_class = RoutineSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Routine.objects.filter(creator=self.request.user)

    # actual decoration engineering here
    def fix_creator(func):
        def wrapper(self, request, *args, **kwargs):
            # set creator to the associated user before proceeding
            request.data.update({"creator": request.user.id})
            return func(self, request, *args, **kwargs)
        return wrapper

    # automatically set creator in requests and make it unmodifiable

    @fix_creator
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @fix_creator
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @fix_creator
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
