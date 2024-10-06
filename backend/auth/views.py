from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, world!"})

# starter endpoints

@api_view(["POST"])
def register(request):
    # process data by instantiating new serializer with given data
    serializer = UserSerializer(data=request.data)
    # now check that the data was valid
    if serializer.is_valid(): # valid if - unique and all fields satisfied
        user = serializer.save() # save data in serializer as model
        user.set_password(request.data["password"]) # hash password
        user.save()
        token = Token.objects.create(user=user)
        # return data (user json, token)
        return Response({
            "token": token.key, # token value (refer to docs for token attributes)
            "user" : serializer.data # serialized data for send back
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):
    return Response({}, status=status.HTTP_200_OK)

@api_view(["GET"])
def validate_token(request):
    return Response({}, status=status.HTTP_200_OK)



