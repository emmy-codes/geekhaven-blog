from django.shortcuts import render
from django.views import generic
from .models import BlogPost

class BlogGrid(generic.ListView):
    queryset = BlogPost.objects.all().order_by('-creation_date')
    template_name = 'geekhaven/templates/index.html'