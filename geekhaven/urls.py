from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# brute force the 404 error for no favicon to return a 204 instead
def dodge_favicon_404(request):
    return HttpResponse(status=204)


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('geekhaven_blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('favicon.ico', dodge_favicon_404),  # Handle requests for favicon.ico
    path('__reload__/', include('django_browser_reload.urls')),
]
