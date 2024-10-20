from rest_framework import serializers
from django.contrib.auth import get_user_model

# serializers used to serialize models/other into data and vice versa
# see drf docs

# user serializer, meta tag specifies what model its based on and what fields
class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model() # fixed insane bug: don't import user! will crash
        # password set with set_password for hashing
        # fields define the attributes that will be validated from req data
        fields = ["id", "username", "email", "password", 
                        "birthday", "weight", "height", "gender"]
