from django.shortcuts import render


def blog_homepage(request):
    return render(request, 'index.html')
