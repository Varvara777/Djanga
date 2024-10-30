from django.forms import ModelForm
from .models import Posts
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = [ 'title','content', 'author', 'author' ]
