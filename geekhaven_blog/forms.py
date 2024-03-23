from django import forms
from .models import CosplaySubmission

class CosplaySubmissionForm(forms.ModelForm):
    class Meta:
        model = CosplaySubmission
        fields = [
            'character',
            'image',
            'description'
        ]