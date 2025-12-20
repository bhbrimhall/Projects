from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    path = models.TextField()
    name = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
class List(models.Model):
    name = models.TextField()
    type = models.TextField()
    description = models.TextField()
    is_public = models.BooleanField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    thumbnail = models.TextField()
    
class Item(models.Model):
    name = models.TextField()
    image = models.TextField()
    list = models.ForeignKey(to=List, on_delete=models.CASCADE)
    rank = models.TextField()
    
class Profile(models.Model):
    image = models.TextField()
    about = models.TextField()
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    username = models.TextField()
    
class Comment(models.Model):
    content = models.TextField()
    list = models.ForeignKey(to=List, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)