from django.shortcuts import render, redirect
from .models import Activity, TimeLog
from datetime import datetime


def index(req):
    activities = Activity.objects.all()
    return render(req, "core/index.html", {'activities': activities})

def newActivity(req):
    return render(req, "core/new_activity.html")

def activityCreated(req):
    
    # if statement handles when no name is given
    
    if req.POST.get("activity-name") == "":
        name = "Untitled"
    else:
        name = req.POST.get("activity-name")
        
    new_activity = Activity(
        name = name
    )
    
    new_activity.save()
    return redirect("/activity/" + str(new_activity.id) + "/")

def viewActivity(req, id):
    activity = Activity.objects.get(pk = id)
    timelogs = activity.timelog_set.all()
    return render(req, "core/activity.html", {'activity': activity, 'timelogs': timelogs})
    
def newTimelog(req, id):
    activity = Activity.objects.get(pk = id)
    return render(req, "core/new_timelog.html", {'activity': activity})
    
def timelogCreated(req, id):
    
    # if statement handles when no values are given for the inputs
    
    if req.POST.get("start-time") != '' and req.POST.get("end-time") != '':
        
        start_time = datetime.strptime(req.POST.get("start-time"), '%Y-%m-%dT%H:%M')
        end_time = datetime.strptime(req.POST.get("end-time"), '%Y-%m-%dT%H:%M')
        
        timelog = TimeLog(
            start_time = str(start_time),
            end_time = str(end_time),
            activity_id = id
        )
        
        timelog.save()
        return redirect('/activity/' + id + "/")
    else:
        return newTimelog(req, id)