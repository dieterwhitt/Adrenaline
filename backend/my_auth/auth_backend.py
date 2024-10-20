from django.contrib.auth.backends import ModelBackend
from my_auth.models import MyUser

# custom authentication backend for accepting username or email login
# need to enforce email uniqueness
class UsernameOrEmailBackend(ModelBackend):
    # overwrite default authenticate
    def authenticate(self, request, identifier=None, password=None, **kwargs):
        # print("authenticating using custom backend:")
        try:
            # try to find the user by username first
            user = MyUser.objects.get(username=identifier)
        except MyUser.DoesNotExist:
            try:
                # if the username doesn't exist, try to find the user by email
                user = MyUser.objects.get(email=identifier)
            except MyUser.DoesNotExist:
                user = None

        # check if the user exists and if the password is correct
        if user is not None and user.check_password(password):
            return user
        return None
