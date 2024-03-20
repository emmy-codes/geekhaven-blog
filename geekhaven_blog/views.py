from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import BlogPost
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


class BlogGrid(generic.ListView):

    template_name = "blogpost_list.html"
    context_object_name = "blogpost_list"
    paginate_by = 6

    def get_queryset(self):
        queryset = BlogPost.objects.filter().order_by("-creation_date")

        """ 
            stores input of search bar text
            (on our input field name=search_query)
        """
        search_query = self.request.GET.get("search_query")

        if search_query:
            """
            filters posts with blog headings that include
            the search query word/s
            """
            queryset = queryset.filter(blog_heading__icontains=search_query)

        return queryset


@csrf_protect
def view_blog_post(request, slug):
    queryset = BlogPost.objects.filter(blog_published_status=1)
    blog_post = get_object_or_404(queryset, url_slug=slug)

    return render(request, "blog_post.html", {"blog_post": blog_post})


@csrf_protect
def register_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()
            # cleaned_data on the form data is created once form is validated
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            # redirects the user once they are authenticated/registered
            return redirect("homepage")
    # if the request is GET instead, display registration form    
    else:
        form = UserCreationForm()
    
        return render(request, "register.html", {"form": form})
