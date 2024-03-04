from django.db import models
from django.contrib.auth.models import User


PUBLISHED_STATUS = ((0, 'Draft'), (1, 'Published'))

class BlogPosts(models.Model):
    blog_header = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    blog_published_status = models.IntegerField(choices=PUBLISHED_STATUS, default=0)
    blog_content = models.TextField
    creation_date = models.DateTimeField(auto_now_add=True)
    blog_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    blog_likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
