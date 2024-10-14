from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
import json
from jsonschema import validate

# loads fitness/data/muscles.json and validates it, then sends it
@api_view(["GET"])
def get_muscles(request):
    # open muscles.json and remove invalid entries
    # schema defines muscle object. in json: "muscle_name" : {muscle_schema}
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
        f = json.load(raw)

    return Response({}, status=status.HTTP_200_OK)

# loads fitness/data/exercises.json and validates it
@api_view(["GET"])
def get_exercises(request):
    # in json: "exercise_name" : {exercise_schema}
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
    return Response({}, status=status.HTTP_200_OK)

