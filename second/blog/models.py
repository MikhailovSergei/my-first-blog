# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title=models.TextField()
	text=models.TextField()
	

#class Comment(models.Model):
#	text=models.CharField(max_length=100)
#	post=models.ForeignKey(Post)