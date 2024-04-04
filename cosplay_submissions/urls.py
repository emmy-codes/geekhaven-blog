from . import views
from django.urls import path

urlpatterns = [
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
    path("edit_submission/<int:pk>/", views.update_submission, name="edit_submission"),
]