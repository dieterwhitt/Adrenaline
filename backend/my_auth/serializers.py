from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..fitness.serializers import RoutineSerializer


# serializers used to serialize models/other into data and vice versa
# see drf docs

# user serializer, meta tag specifies what model its based on and what fields
# from drf docs: birthday format = "YYYY-MM-DD"
class MyUserSerializer(serializers.ModelSerializer):
    # get routines associated with user
    routines = RoutineSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model() # fixed insane bug: don't import user! will crash
        # password set with set_password for hashing
        # fields define the attributes that will be validated from req data
        # first and last name are optional
        fields = ["id", "username", "email", "password", "birthday", "weight", 
                         "height", "gender", "first_name", "last_name", "routines"]
