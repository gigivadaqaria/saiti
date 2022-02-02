from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import  User, POST,comment, Topic
from django import forms

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        post = super().save(commit=False)
        post.host = self.user

        if commit:
            post.save()

        return post


    class Meta:
        model = POST
        exclude = ['host']

class CommentForm(ModelForm):
    

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        post = super().save(commit=False)
        comment.host = self.user

 
        if commit:
            post.save()

        return post

    class Meta:
        model = comment
        exclude = ['host', ]
        
class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields ='__all__'


