from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "username",
            "password",
			"email"
        ]


# If you don't do this you cannot use Bootstrap CSS class
'''
class LoginForm(AuthenticationForm):     
	username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name':
								'username'})) 
	password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
								'name': 'password'}))
'''