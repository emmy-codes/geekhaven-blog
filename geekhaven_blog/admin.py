from django.contrib import admin
from .models import BlogPost, BlogComments  #  AboutGeekHaven, SearchBar

admin.site.register(BlogPost)
admin.site.register(BlogComments)
# admin.site.register(AboutGeekHaven)
# admin.site.register(SearchBar)
