from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import CosplaySubmission
from .forms import CosplaySubmissionForm
from django.contrib import messages


@csrf_protect
def cosplay_submissions(request):
    # place for users to upload their cosplays
    if request.method == "POST":
        # request.FILES is how Django handles file uploads
        cosplay_submission_form = CosplaySubmissionForm(
            request.POST, request.FILES
        )
        if cosplay_submission_form.is_valid():
            # create form submission without submitting
            cosplay_submission = cosplay_submission_form.save(
                commit=False
            )
            cosplay_submission.author = request.user
            cosplay_submission.approval_state = False
            cosplay_submission.save()
            messages.success(
                request,
                "Your submission has been sent to an admin and is pending approval",  # noqa
            )
            return redirect("cosplay_hall_of_fame")
    else:
        cosplay_submission_form = CosplaySubmissionForm()
        return render(
            request,
            "cosplay_submissions.html",
            {"cosplay_submission_form": cosplay_submission_form},
        )


@csrf_protect
def cosplay_hall_of_fame(request):
    # showing all published submissions publicly
    published_submissions = CosplaySubmission.objects.filter(
        approval_state=True
    )

    # shows pending submissions when authenticated to the specific user
    if request.user.is_authenticated:
        user_submissions = CosplaySubmission.objects.filter(
            author=request.user, approval_state=False
        )
    else:
        user_submissions = []

    # renders published submissions to all, and drafts to their respective user
    return render(
        request,
        "cosplay_hall_of_fame.html",
        {
            "published_submissions": published_submissions,
            "user_submissions": user_submissions,
        },
    )


@csrf_protect
# allows edit and delete on user submission
def update_submission(request, pk):
    # ensuring request is from the post author
    submission = get_object_or_404(
        CosplaySubmission, pk=pk, author=request.user
    )

    if request.method == "POST":
        form = CosplaySubmissionForm(
            request.POST, request.FILES, instance=submission
        )
        if form.is_valid():
            form.save()
            submission.approval_state = False
            submission.save(update_fields=["approval_state"])
            messages.success(
                request, "Your submission has been updated and is pending admin appoval"  # noqa
            )
            return redirect("cosplay_hall_of_fame")
    else:
        # create form containing the selected instance of cosplay submission
        form = CosplaySubmissionForm(instance=submission)

    return render(
        request, "cosplay_submissions.html", {"cosplay_submission_form": form}
    )


""" Edit the pending or published cosplay submission by sending the user to the
cosplay_submission form with the data from the appended submission """


@csrf_protect
def edit_submission(request, pk):

    submission = get_object_or_404(CosplaySubmission, pk=pk)
    form = CosplaySubmissionForm(instance=submission)

    return render(
        request,
        "cosplay_submissions.html",
        {"form": form, "submission": submission, "edit_mode": True},
    )


@csrf_protect
def delete_submission(request, pk):

    submission = get_object_or_404(
        CosplaySubmission, pk=pk, author=request.user
    )
    submission.delete()
    return redirect("cosplay_hall_of_fame")
