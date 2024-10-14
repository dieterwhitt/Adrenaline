from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
import json
from jsonschema import validate, ValidationError

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
                    "enum": ["Calves", "Hamstrings", "Quadriceps", "Biceps", "Triceps",
                            "Forearms", "Traps","Lats"]
                },
                "male_segment": {"type" : "int"},
                "female_segment": {"type" : "int"},
            },
            "required": ["id", "group", "male_segment", "female_segment"]
        }
        with open("./data/muscles.json", "r") as raw:
            muscles = json.load(raw)
        
        for name, data in muscles:
            try:
                validate(instace=data, schema=muscle_schema)
            except ValidationError as ve:
                # issue with muscle data: delete entry from output
                print(ve)
                del muscles[name]
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
                        "type" : "String"
                    }
                },
                "category": {
                    "enum": ["Aerobic", "Anaerobic", "Strength", "Flexibility"]
                }
            }
        }
        with open("./data/exercises.json", "r") as raw:
            exercises = json.load(raw)
        
        for name, data in exercises:
            try:
                validate(instace=data, schema=exercise_schema)
            except ValidationError as ve:
                # issue with exercise data: delete entry from output
                print(ve)
                del exercises[name]
        return Response(exercises, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
