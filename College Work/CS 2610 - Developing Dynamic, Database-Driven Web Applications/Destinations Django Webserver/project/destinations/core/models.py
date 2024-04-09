from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    email = models.TextField(unique=True)
    password_hash = models.TextField()

class Session(models.Model):
    token = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
class Destination(models.Model):
    name = models.TextField()
    review = models.TextField()
    rating = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_publicly = models.BooleanField()
    id = models.BigAutoField(primary_key=True)