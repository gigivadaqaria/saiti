from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import  User, POST,comment


class PostForm(ModelForm):
    class Meta:
        model = POST
        fields = ['title', 'body', 'host', 'topic', 'background_image']

class CommentForm(ModelForm):
    class Meta:
        model = comment
        fields = '__all__'



