from __future__ import unicode_literals
from django.db import models
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