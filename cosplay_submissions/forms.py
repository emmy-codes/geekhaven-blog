from django import forms
from .models import CosplaySubmission


class CosplaySubmissionForm(forms.ModelForm):
    class Meta:
        model = CosplaySubmission
        fields = ["character", "image", "description"]
        """
            Widgets to customize the appearance of the fields above.
            Attrs are mostly classes with the standard input placeholder text
        """
        widgets = {
            "image": forms.FileInput(
                attrs={
                    "class": "block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",  # noqa
                }
            ),
            "character": forms.TextInput(
                attrs={
                    "class": "block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",  # noqa
                    "placeholder": "Character Name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",  # noqa
                    "placeholder": "Description",
                }
            ),
        }
