from django.contrib import admin
from django.urls import path
from rest_framework import routers
import my_auth.views
import fitness.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello_world", my_auth.views.hello_world),
    path("register", my_auth.views.register),
    path("login", my_auth.views.login),
    path("validate_token", my_auth.views.validate_token),
    path("get_muscles", fitness.views.get_muscles),
    path("get_exercises", fitness.views.get_exercises),
]

# crud patterns

# {prefix}/ get: list, post: create
# {prefix}/{id} get: retrieve, put: update, patch: partial update, delete: delete

# see drf router docs. have to register with basename
router = routers.SimpleRouter()
router.register(r"exercise", fitness.views.ExerciseViewSet, basename="exercise")
router.register(r"workout", fitness.views.WorkoutViewSet, basename="workout")
router.register(r"routine", fitness.views.RoutineViewSet, basename="routine")

# add viewset patterns
urlpatterns += router.get_urls()