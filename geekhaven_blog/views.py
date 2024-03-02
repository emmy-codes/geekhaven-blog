from django.shortcuts import render
from django.http import HttpResponse


def blog_homepage(request):
    return HttpResponse("Testing 123!")
