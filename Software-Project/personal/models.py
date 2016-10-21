from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here

#Sample Model
'''
class Post(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=10)
	email = models.EmailField(max_length=70,blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.email

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})
'''