from django.contrib import admin
from .models import BlogPost, BlogComment, CosplaySubmission
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
# passing in SummernoteModelAdmin allows for use of summernote on admin panel
class AdminSearchOption(SummernoteModelAdmin):
    search_options = (
        "blog_heading",
        "url_slug",
        "blog_published_status",
        "creation_date",
    )
    search_by_heading = ["blog_heading"]
    search_filter = ("blog_published_status",)
    prepopulated_fields = {
        # slug field(url creator) is automatically populated using the blog title
        "url_slug": ("blog_heading",)
    }
    summernote_text_fields = (
        # assigns the use of summernote only to the blog_content field
        "blog_content"
    )

class AdminApproveCosplaySubmissions(admin.ModelAdmin):
    list_display = (
        'author',
        'character',
        'submission_date',
        'submission_status'
    )
    
    actions = ['approve_cosplay_submissions']
    def approve_cosplay_submissions(self, request, queryset):
        queryset.update(submission_status=1)

# admin.site.register(BlogComment)
admin.site.register(CosplaySubmission, AdminApproveCosplaySubmissions)