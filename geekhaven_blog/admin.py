from django.contrib import admin
from .models import BlogPost, CosplaySubmission
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
# passing in SummernoteModelAdmin allows for use of summernote on admin panel
class AdminSearchOption(SummernoteModelAdmin):
    search_options = (
        "blog_heading",
        "url_slug",
        "blog_approved_status",
        "creation_date",
    )
    search_by_heading = ["blog_heading"]
    search_filter = ("blog_approved_status",)
    prepopulated_fields = {
        "url_slug": ("blog_heading",)
    }
    summernote_text_fields = (
        # assigns the use of summernote only to the blog_content field
        "blog_content"
    )


class AdminApproveCosplaySubmissions(admin.ModelAdmin):
    list_display = ("author", "character", "submission_date", "approval_state")

    actions = ["approve_cosplay_submissions"]

    def approve_cosplay_submissions(self, request, queryset):
        queryset.update(approval_state=True)


# admin.site.register(BlogComment)
admin.site.register(CosplaySubmission, AdminApproveCosplaySubmissions)
