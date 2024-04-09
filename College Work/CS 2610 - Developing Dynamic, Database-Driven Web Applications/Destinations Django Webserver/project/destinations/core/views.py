from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from .models import Destination, User, Session
import hashlib
import string
import random

def index(req):
    # decide wether to render the log out and my destinations links or the create account and sign in links
    if req.user == None:
        logged_in = False
    else:
        logged_in = True
    
    public_destinations = list(Destination.objects.filter(share_publicly=True))
    trimmed_destinations = []
    
    #trim the list to the most recent 5
    i = 0
    while len(trimmed_destinations) < 5:
         trimmed_destinations.append(public_destinations[len(public_destinations) - 1 - i])
         i += 1
    
    return render(req, "core/index.html", {'destinations': trimmed_destinations, 'logged_in': logged_in})

def newUser(req):
    return render(req, "core/new_user.html")

def createUser(req):

    if '@' in req.POST.get("new_email"):
        if len(req.POST.get('new_password')) >= 8:
            
            contains_num = False
            for char in req.POST.get('new_password'):
                 if char.isdigit():
                     contains_num = True
                     break
            
            if contains_num:
                
                #passed all the tests
                
                password_hash = hashlib.sha256(bytes(req.POST.get("new_password"), "UTF-8")).hexdigest()
                new_user = User(
                    name = req.POST.get("new_name"),
                    email = req.POST.get("new_email"),
                    password_hash = password_hash
                    )
            else:
                return HttpResponseBadRequest('You really think that was a good password? You need a number you goofy.')
        else:
            return HttpResponseBadRequest('Come on. You can do better than eight characters.')
    else:
        return HttpResponseBadRequest("That's not a valid email. You at least need an '@'!")
    
    # try to save new user
    try:
        new_user.save()
    except:
        return HttpResponseBadRequest("A user with that email already exists! Go try again.")
    
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    
    #create session
    session = Session(token=hashlib.sha256(bytes(token, "UTF-8")).hexdigest(), user=new_user)
    session.save()
    
    #add token cookie
    res = redirect('/destinations/')
    res.set_cookie('token', token)
    
    return res

def destinations(req):
    if req.method == "POST":
        
        #create new destination
        
        if req.POST.get("public") == "on":
            public = True
        else:
            public = False
            
        new_destination = Destination(name = req.POST.get("name"),
                                      review = req.POST.get("review"),
                                      rating = req.POST.get("rating"),
                                      user = req.user,
                                      share_publicly = public)
        
        new_destination.save()
        
    # get users destinations
    my_destinations = Destination.objects.filter(user = req.user)
    return render (req, "core/destinations.html", {'my_destinations': my_destinations, 'username': req.user.name})

def newDestination(req):
    return render (req, "core/new_destination.html")

def viewDestination(req, id):
    
    # see if the user owns the destination and that it exists
    try:
        destination = Destination.objects.get(user=req.user, pk=id)
    except:
        return HttpResponseNotFound()
    
    if req.method == "POST":
        
        #update destination
        
        if req.POST.get("public") == "on":
            public = True
        else:
            public = False
            
        destination.name = req.POST.get("name")
        destination.review = req.POST.get("review")
        destination.rating = req.POST.get("rating")
        destination.share_publicly = public
        
        destination.save()
        return redirect("/destinations/")
    
    return render(req, "core/view_destination.html", {'destination': destination})

def deleteDestination(req, id):
    # make sure the user owns the destination that they are trying to delete
    # and make sure the destination actually exists
    try:
        destination = Destination.objects.get(user=req.user, pk=id)
        destination.delete()
    except:
        return HttpResponseNotFound()
    
    return redirect("/destinations/")
    
def newSession(req):
    
    # decide wether to render the log out and my destinations links or the create account and sign in links
    if req.user == None:
        logged_in = False
    else:
        logged_in = True
    
    return render(req, 'core/new_session.html', {'logged_in': logged_in})

def createSession(req):
    
    # see if the email is valid
    try:
        user = User.objects.get(email=req.POST.get("email"))
    except:
        return HttpResponseNotFound()
    
    #check the password
    if hashlib.sha256(bytes(req.POST.get("password"), "UTF-8")).hexdigest() != user.password_hash:
        return HttpResponseNotFound()
    
    # create session
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    session = Session(token=hashlib.sha256(bytes(token, "UTF-8")).hexdigest(), user=user)
    session.save()
    
    #add token cookie
    res = redirect('/destinations/')
    res.set_cookie('token', token)
    return res

def deleteSession(req):
    
    # find and delete user's session
    session = Session.objects.get(pk=req.user)
    session.delete()
  
    res = redirect("/")
    res.delete_cookie('token')
    return res
