from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.BlogGrid.as_view(), name="homepage"),
    path("accounts/", include("allauth.urls")),
    path("<slug:slug>/", views.view_blog_post, name="view_blog_post"),
    path("register/", views.register_account, name="register"),
    path("login/", views.login, name="login")
]
