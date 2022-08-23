from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100,unique=True,blank=True,null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)

    def __str__(self):
        return self.id

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=True)
    message = models.TextField(max_length=500,blank=False,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    time = models.DateTimeField(auto_now_add=True)
    received = models.BooleanField(default=False,null=True)
