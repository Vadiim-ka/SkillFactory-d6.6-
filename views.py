from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'post.html'
    context_object_name = 'post'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'
