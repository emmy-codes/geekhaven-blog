from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BlogPost


class BlogGrid(generic.ListView):
    queryset = BlogPost.objects.all().order_by('-creation_date')
    template_name = 'blogpost_list.html'
    context_object_name = 'blogpost_list'


def view_blog_post(request, slug):
    queryset = BlogPost.objects.filter(blog_published_status=1)
    blog_post = get_object_or_404(queryset, url_slug=slug)
    paginate_by = 9
    return render(request, 'blog_post.html',
                  {'blog_post': blog_post})
