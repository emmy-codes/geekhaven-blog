"""
URL configuration for geekhaven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# brute force the 404 error for no favicon to return a 204 instead
def dodge_favicon_404(request):
    return HttpResponse(status=204)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('geekhaven_blog.urls')),
    path('summernote/', include('django_summernote.urls')), 
    path('favicon.ico', dodge_favicon_404),  # Handle requests for favicon.ico
    path('__reload__/', include('django_browser_reload.urls')),
]