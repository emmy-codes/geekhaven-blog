from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.shortcuts import render


PUBLISHED_STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):
    blog_heading = models.CharField(max_length=250, unique=True)
    heading_image = CloudinaryField("image", default="placeholder")
    url_slug = models.SlugField(max_length=250, unique=True, blank=True)
    blog_published_status = models.IntegerField(choices=PUBLISHED_STATUS, default=0)
    blog_content = models.TextField(default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    content_updated_on = models.DateTimeField(auto_now_add=True)

    # stores ref to the User that is the author of the post.
    blog_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # blank=True means the field is not required
    blog_likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)

    # to give a preview text on the post icons on the main page
    blog_excerpt = models.TextField(default="", blank=True)

    class Meta:
        ordering = ["-creation_date"]

    # changes object name on admin site to blog_heading of blog
    def __str__(self):
        return self.blog_heading


class BlogComment(models.Model):
    comment_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_commenter"
    )
    comment_body = models.TextField(default="")
    comment_approved = models.BooleanField(default=False)
    comment_which_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="post_comments"
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["creation_date"]

    # shows the comment and commenter on admin comment page
    def __str__(self):
        return f"Comment: {self.comment_body} | by {self.comment_author}"

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    
# unique model - cosplay submissions for users to utilise CRUD on the UI

class CosplaySubmission(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # user can upload their own images
    image = CloudinaryField("image")
    # who the user is cosplaying as
    character = models.CharField(max_length=150, blank=False)
    submission_status = models.IntegerField(choices=PUBLISHED_STATUS, default=0)
    submission_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=False)
    approval_state = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.author.username} cosplaying as {self.character}"