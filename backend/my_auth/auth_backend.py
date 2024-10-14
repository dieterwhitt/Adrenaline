from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

# custom authentication backend for accepting username or email login
# need to enforce email uniqueness
class UsernameOrEmailBackend(ModelBackend):
    # overwrite default authenticate
    def authenticate(self, request, identifier=None, password=None, **kwargs):
        # print("authenticating using custom backend:")
        try:
            # try to find the user by username first
            user = User.objects.get(username=identifier)
        except User.DoesNotExist:
            try:
                # if the username doesn't exist, try to find the user by email
                user = User.objects.get(email=identifier)
            except User.DoesNotExist:
                user = None

        # check if the user exists and if the password is correct
        if user is not None and user.check_password(password):
            return user
        return None
