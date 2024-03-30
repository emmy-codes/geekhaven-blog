from . import views
from django.urls import path, include

urlpatterns = [
    path("register/", views.register_account, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("accounts/", include("allauth.urls")),
    path(
        "cosplay_hall_of_fame/",
        views.cosplay_hall_of_fame,
        name="cosplay_hall_of_fame"
    ),
    path(
        "cosplay_submissions/",
        views.cosplay_submissions,
        name="cosplay_submissions"
    ),
    path("", views.BlogGrid.as_view(), name="homepage"),
    path("<slug:slug>/", views.view_blog_post, name="view_blog_post"),
]
