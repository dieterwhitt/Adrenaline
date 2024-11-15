"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
# see drf router docs. have to register with basename
router = routers.SimpleRouter()
router.register(r"exercises", fitness.views.ExerciseViewSet, basename="exercise")
router.register(r"workouts", fitness.views.WorkoutViewSet, basename="workout")
router.register(r"routines", fitness.views.RoutineViewSet, basename="routine")

# add viewset patterns
urlpatterns += router.get_urls()