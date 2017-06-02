# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.http import HttpResponse
from second.blog.models import Post

class PostListView(ListView):
    template_name='blog/blog.html'
    model=Post
    context_object_name='post_list'
    
# Create your views here.
