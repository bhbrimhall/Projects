from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from core.models import Profile


def sign_up(req):
    if req.method == "POST":
        
        if req.POST.get("username") and req.POST.get("password") and req.POST.get("email") and req.POST.get("first_name") and req.POST.get("last_name"):
            user = User.objects.create_user(
                username=req.POST.get("username"),
                password=req.POST.get("password"),
                email=req.POST.get("email"),
                first_name=req.POST.get("first_name"),
                last_name=req.POST.get("last_name"),
            )
            profile = Profile(image="profile",
                            about="",
                            user = user,
                            username = req.POST.get("username"))
            profile.save()
            login(req, user)
            return redirect("/")
        else:
            return render(req, "registration/sign_up.html")
    else:
        return render(req, "registration/sign_up.html")

def sign_in(req):
    if req.method == "POST":
        user = authenticate(req, username=req.POST.get("username"), password=req.POST.get("password"))
        
        if user is not None:
            login(req, user)
            return redirect("/")

        return render(req, "registration/sign_in.html")
    else:
        return render(req, "registration/sign_in.html")

def logout_view(request):
    logout(request)
    return JsonResponse({"success": True })