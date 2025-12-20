from django.shortcuts import render
from django.conf  import settings
import json
import os
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from .models import List, Item, Image, Profile, Comment
import secrets
import random
from pathlib import Path


# Load manifest when server launches
MANIFEST = {}
if not settings.DEBUG:
    f = open(f"{settings.BASE_DIR}/core/static/manifest.json")
    MANIFEST = json.load(f)

# Create your views here.
def index(req):
    context = {
        "asset_url": os.environ.get("ASSET_URL", ""),
        "debug": settings.DEBUG,
        "manifest": MANIFEST,
        "js_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["file"],
        "css_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["css"][0]
    }
    return render(req, "core/index.html", context)


def get_user(req):           
    if req.user.is_authenticated:
        profile = Profile.objects.get(user=req.user)
        return JsonResponse({"user": model_to_dict(req.user), "success": True, "profile": model_to_dict(profile)})
    else:
        return JsonResponse({"success": False })

@login_required
def create_list(req):
    body = json.loads(req.body)
    if body['listType'] == 'tier' or body['listType'] == 'raw':
        if type(body['title']) == str:
            try:
                list = List(
                    name=body['title'], 
                    type=body['listType'], 
                    description="", 
                    is_public=False, 
                    user=req.user, 
                    thumbnail=body['listType']
                    )
                list.save()
                
                return JsonResponse({"success": True, "id": list.id})
            except:
                return JsonResponse({"success": False})
        
    return JsonResponse({"success": False})

def view_list(req, id):
    try:
        list = List.objects.get(id=id)
        
        items = Item.objects.filter(list=list)
        items = [model_to_dict(item) for item in items]
        
        filtered_items = []
        for i in items:
            if i["rank"] != "":
                filtered_items.append(i)
                
        user = list.user
        
        return JsonResponse({"list": model_to_dict(list), "items": filtered_items, "user": model_to_dict(user), "success": True})
    except:
        return JsonResponse({"success": False})

@login_required
def edit_list(req, id):
    try:
        list = List.objects.get(id=id, user=req.user)
        items = Item.objects.filter(list=list)
        items = [model_to_dict(item) for item in items]
        return JsonResponse({"list": model_to_dict(list), "items": items, "success": True})
    except:
        return JsonResponse({"success": False})
    
@login_required
def my_lists(req):
    try:
        lists = List.objects.filter(user=req.user)            
        lists = [model_to_dict(list) for list in lists]
        return JsonResponse({"lists": lists, "success": True})
    except:
        return JsonResponse({"success": False})

@login_required
def add_item(req):
    try:
        body = json.loads(req.body) 
        list = List.objects.get(id=body["list_id"], user=req.user)
        item = Item(name = body["name"],
                    list = list,
                    rank = '',
                    image = body["image"],
                    )

        item.save()
        return JsonResponse({"success": True, "item": model_to_dict(item)})
    except:
        return JsonResponse({"success": False })

@login_required
def delete_item(req, id):
    try:
        item = Item.objects.get(id=id)
        if not item.list.user == req.user:
            return JsonResponse({"success": False})
        item.delete()
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})
    
@login_required
def update_items(req):
    try:
        body = json.loads(req.body)
        for new_item in body:
            item = Item.objects.get(id=new_item["id"])
            item.rank = new_item["rank"]
            item.save()
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})
    
@login_required
def configure_list(req):
    try: 
        body = json.loads(req.body)
        list = List.objects.get(user = req.user, id=body['id'])
        list.name = body['name']
        list.description = body['description']
        list.is_public = body['is_public']
        list.thumbnail = body['thumbnail']
        list.save()
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})
    
@login_required
def upload_image(req):
    try:
        new_file_name = secrets.token_hex(16)
        extension = req.FILES["my_file"].name.split(".", maxsplit=1)[1]
        file_path = f"/uploaded_images/{new_file_name}.{extension}"
        image = Image(
            name=req.FILES["my_file"].name,
            path=file_path,
            user=req.user
        )
        image.save()

        with open(f"{Path.cwd()}{file_path}", "ab+") as f:
            for chunk in req.FILES["my_file"].chunks():
                f.write(chunk)
        return JsonResponse({"success": True, "image": image.id})

    except:
         return JsonResponse({"success": False})

@login_required
def my_images(req):
    try:
        images = Image.objects.filter(user=req.user)
        images = [model_to_dict(img) for img in images]
        return JsonResponse({"success": True, "images": images})
    except:
        return JsonResponse({"success": False})
    
def get_image(req, id):
    try:
        if id == 'item':
            f = open(f"{Path.cwd()}/uploaded_images/no-img.png", "rb")
        elif id == 'raw':
            f = open(f"{Path.cwd()}/uploaded_images/raw.png", "rb")
        elif id == 'tier':
            f = open(f"{Path.cwd()}/uploaded_images/tier.png", "rb")
        elif id == "profile":
            f = open(f"{Path.cwd()}/uploaded_images/profile.png", "rb")
        else:
            image = Image.objects.get(id=id)
            f = open(f"{Path.cwd()}{image.path}", "rb")
            
        return FileResponse(f, as_attachment=True)
    except:
        f = open(f"{Path.cwd()}/uploaded_images/no-img.png", "rb")
        return FileResponse(f, as_attachment=True)
    
@login_required
def delete_image(req, id):
    try:
        image = Image.objects.get(user=req.user, id=id)
        os.remove(f"{Path.cwd()}{image.path}")
        image.delete()
        return JsonResponse({"success": True})
    except: 
        return JsonResponse({"success": False})
    
def get_list_images(req, id):
    try:
        list = List(is_public=True, id=id)
        items = Item.objects.filter(list=list)
        
        filtered_items = []
        for i in items:
            if i.rank != "":
                filtered_items.append(i)
            
        list_images = []
        for i in filtered_items:
            if not i.image == None:
                list_images.append(i.image)
                
        list_images = [model_to_dict(img) for img in list_images]
        
        return JsonResponse({"success": True, "images": list_images})
    except: 
        return JsonResponse({"success": False })

def get_profile(req, id):
    try:
        profile = Profile.objects.get(id=id)
        lists = List.objects.filter(user = profile.user, is_public = True)
        lists = [model_to_dict(list) for list in lists]
        return JsonResponse({"success": True, "profile": model_to_dict(profile), "lists": lists })
    except:
        return JsonResponse({"success": False })

@login_required
def configure_profile(req):
    try:
        body = json.loads(req.body)
        profile = Profile.objects.get(user = req.user)
        profile.about = body["about"]
        profile.image = body["image"]
        profile.save()
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False })

@login_required
def comment(req, id):
    try:
        body = json.loads(req.body)
        list = List.objects.get(id=id)
        profile = Profile.objects.get(user = req.user)
        comment = Comment(
            content=body["content"],
            list = list,
            user = req.user,
            profile = profile
            )
        comment.save()   
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False })

def get_comments(req, id):
    try:
        list = List.objects.get(id=id)
        comments = Comment.objects.filter(list = list)
        comments_list = []
        for comment in comments:
            profile_img = comment.profile.image
            comment_dict = model_to_dict(comment)
            comment_dict['profile_img'] = profile_img
            comment_dict['username'] = comment.profile.username
            comments_list.append(comment_dict) 
            
        return JsonResponse({"success": True, "comments": comments_list})
    except:
        return JsonResponse({"success": False })

def get_featured_lists(req):
    try:
        lists = List.objects.filter(is_public = True)
        while len(lists) > 30:
            lists.pop(random.randrange(len(lists))) 
        lists_list = []
        for list in lists:
            profile = Profile.objects.get(user = list.user)
            list_dict = model_to_dict(list)
            list_dict["username"] = profile.username
            list_dict["profile"] = profile.id
            lists_list.append(list_dict)
            
        return JsonResponse({"success": True, "lists": lists_list})
    except:
        return JsonResponse({"success": False })

def search(req):
    try:
        body = json.loads(req.body)
        lists = List.objects.filter(name__contains = body['searchValue'], is_public=True)
        profiles = Profile.objects.filter(username__contains = body['searchValue'])
        lists = [model_to_dict(list) for list in lists]
        profiles = [model_to_dict(profile) for profile in profiles]
        return JsonResponse({"success": True, "lists": lists, "profiles": profiles})
    except:
        return JsonResponse({"success": False })