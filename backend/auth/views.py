from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# currently using token authentication. will probably switch to session at some point

@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, world!"})

# starter endpoints
# {username, password, email}
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
            "token": token.key,
            "user" : serializer.instance
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# {username, password}
# currently using django's default model backends for authentication.
# can define my own later (ex. login with email OR username)
@api_view(["POST"])
def login(request):
    # attempt to get user associate with username and check if password matches.
    # if valid, return token
    user = authenticate(username=request.data["username"], password=request.data["password"])
    if user is not None:
        # retrieve token (create it if it wasn't created for any reason)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user) # (instance is an existing object)
        return Response({
            "token": token.key, # token value (refer to docs for token attributes)
            "user" : serializer.data # serialized data for send back
        }, status=status.HTTP_200_OK)
    else:
        # not valid
        return Response({}, status=status.HTTP_404_NOT_FOUND)

# header:
# Authorization : token
# returns the appropriate error resopnse if invalid
# decorators are necessary to identify and validate user
@api_view(["GET"])
# auth method, verifies user
@authentication_classes([SessionAuthentication, TokenAuthentication])
# grants access to the view if the user is authenticated
@permission_classes([IsAuthenticated])
def validate_token(request):
    # request.user and request.auth automatically provided by TokenAuthentication class
    # with request using auth token
    # see drf token docs
    user = request.user
    return Response({"message": f"passed for {user.username if user.username else "Anonymous"}"},
                     status=status.HTTP_200_OK)
#


