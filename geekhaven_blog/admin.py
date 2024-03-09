from django.contrib import admin
from .models import BlogPost, BlogComment  #  AboutGeekHaven, SearchBar
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class AdminSearchOption(SummernoteModelAdmin):  # passing in SummernoteModelAdmin allows for use of summernote on the admin panel
    search_options = ('blog_heading', 'url_slug', 'blog_published_status')
    search_by_heading = ['blog_heading']
    search_filter = ('blog_published_status',)
    prepopulated_fields = {'url_slug': ('blog_heading',)}  # slug field (url creator) is automaticelly populated using the blogs' title
    summernote_text_fields = ('blog_content') # assigns the use of summernote only to the blog_content field


admin.site.register(BlogComment)
# admin.site.register(AboutGeekHaven)
# admin.site.register(SearchBar)
