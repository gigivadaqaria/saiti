from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here
from django.contrib.auth.models import AbstractUser

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class POST(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=3000)
    background_image = models.ImageField(null = True,upload_to='posts/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title

class comment(models.Model):
    post = models.ForeignKey(POST,related_name="comments", on_delete=models.SET_NULL, null=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField(max_length=200)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return self.body



        
    


