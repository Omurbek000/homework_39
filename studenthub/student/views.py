from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import TempForm

# Create your views here.


def temp_view(request):
    if request.method == "POST":
        form = TempForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            message = form.cleaned_data["text"]

            messages.success(request, f"We got your inputs!{email} and {message}")

            return redirect("temp_form")
    else:
        form = TempForm()

    return render(request, "student/temp_template.html", {"form": form})
