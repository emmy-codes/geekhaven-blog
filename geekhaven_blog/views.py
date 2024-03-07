from django.shortcuts import render
from django.views import generic
from .models import BlogPost

class BlogGrid(generic.ListView):
    model = BlogPost