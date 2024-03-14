from . import views
from django.urls import path

urlpatterns = [
    path("", views.BlogGrid.as_view(), name="homepage"),
    path("<slug:slug>/", views.view_blog_post, name="view_blog_post"),
]
