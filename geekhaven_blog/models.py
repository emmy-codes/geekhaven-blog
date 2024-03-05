from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


PUBLISHED_STATUS = ((0, 'Draft'), (1, 'Published'))

class BlogPost(models.Model):
    blog_heading = models.CharField(max_length=250, unique=True)
    heading_image = CloudinaryField('image', default='placeholder')
    url_slug = models.SlugField(max_length=250, unique=True)
    blog_published_status = models.IntegerField(choices=PUBLISHED_STATUS, default=0)
    blog_content = models.TextField(default='')
    creation_date = models.DateTimeField(auto_now_add=True)
    content_updated_on = models.DateTimeField(auto_now_add=True)
    blog_author = models.ForeignKey( # stores ref to the User that is the author of the post.
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    blog_likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)  # blank=True means the field is not required
    blog_excerpt = models.TextField(default='', blank=True)  # to give a preview text on the post icons on the main page


class BlogComments(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment_body = models.TextField(default='', blank=True)
    comment_approved = False
    comment_which_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comment')