from rest_framework import serializers
from django.contrib.auth.models import User

# using built in user model
# and using the rest framework's model serializers

# serializers used to serialize models/other data

# user serializer, meta tag specifies what model its based on and what fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # password set with set_password for hashing
        # fields define the attributes that will be validated from req data
        fields = ["id", "username", "password", "email"] 