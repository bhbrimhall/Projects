from django.urls import path
from . import views

urlpatterns = [
    path("", view = views.index),
    path("users/new/", view = views.newUser),
    path("users/", view=views.createUser),
    path("destinations/", view=views.destinations),
    path("destinations/new/", view=views.newDestination),
    path("destinations/<id>/", view=views.viewDestination),
    path("destinations/<id>/destroy/", view=views.deleteDestination),
    path("sessions/new/", view=views.newSession),
    path("sessions/", view=views.createSession),
    path("sessions/destroy/", view=views.deleteSession)
]