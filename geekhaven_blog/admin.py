from django.contrib import admin
from .models import BlogPost, BlogComment  #  AboutGeekHaven, SearchBar

admin.site.register(BlogPost)
admin.site.register(BlogComment)
# admin.site.register(AboutGeekHaven)
# admin.site.register(SearchBar)
