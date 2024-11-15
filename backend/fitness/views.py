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

# now: class views for exercise, workout, routine (CRUD)
'''
class ExerciseViewSet(APIView):
    # instead of decorators, specify authentication and permissions here
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # get, post, put, delete (CRUD)
    # read
    def get(self, request, id):
        pass
    # create
    def post(self, request):
        pass
    # update
    def put(self, request, id):
        pass
    # delete
    def delete(self, request, id):
        pass

'''

# instead of apiview: use viewsets for abstract crud monkeying

class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # define the list of db rows to include in queryset
    # user matches request user (authenticated)
    def get_queryset(self):
        return Exercise.objects.filter(workout__routine__user=self.request.user)


class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Workout.objects.filter(routine__user=self.request.user)

class RoutineViewSet(viewsets.ModelViewSet):
    serializer_class = RoutineSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Routine.objects.filter(user=self.request.user)
    
