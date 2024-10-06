from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, world!"})

# starter endpoints

@api_view(["POST"])
def register(request):
    return Response({}, status=status.HTTP_200_OK)

@api_view(["POST"])
def login(request):
    return Response({}, status=status.HTTP_200_OK)

@api_view(["GET"])
def validate_token(request):
    return Response({}, status=status.HTTP_200_OK)



