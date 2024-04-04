from django.contrib import admin
from .models import CosplaySubmission

class AdminApproveCosplaySubmissions(admin.ModelAdmin):
    list_display = (
        "author",
        "character",
        "submission_date",
        "approval_state"
    )

    actions = ["approve_cosplay_submissions"]

    def approve_cosplay_submissions(self, request, queryset):
        queryset.update(approval_state=True)

admin.site.register(CosplaySubmission, AdminApproveCosplaySubmissions)