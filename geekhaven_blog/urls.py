from . import views
from django.urls import path, include

urlpatterns = [
    path("register/", views.register_account, name="register"),
    path("accounts/", include("allauth.urls")),
    path("", views.BlogGrid.as_view(), name="homepage"),
    path("<slug:slug>/", views.view_blog_post, name="view_blog_post"),
    path("login/", views.login, name="login"),
]
