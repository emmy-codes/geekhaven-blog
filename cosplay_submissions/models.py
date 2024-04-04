from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# unique model - cosplay submissions for users to utilise CRUD on the UI


class CosplaySubmission(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # user can upload their own images
    image = CloudinaryField("image")
    # who the user is cosplaying as
    character = models.CharField(max_length=150, blank=False)
    submission_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=False)
    approval_state = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author.username} cosplaying as {self.character}"