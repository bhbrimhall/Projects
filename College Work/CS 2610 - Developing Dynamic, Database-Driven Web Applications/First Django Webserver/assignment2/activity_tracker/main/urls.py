from django.urls import path
from . import views
urlpatterns = [
    path("", view = views.index),
    path("new_activity/", view = views.newActivity),
    path("activity-created/", view = views.activityCreated),
    path("activity/<id>/", view=views.viewActivity),
    path("activity/<id>/new_timelog/", view=views.newTimelog),
    path("timelog-created/<id>/", view=views.timelogCreated)
]