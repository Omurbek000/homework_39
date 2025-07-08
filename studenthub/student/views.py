from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import TempForm

# Create your views here.


def temp_form(request):
    print("test")

    # session
    request.session["Teksheryy"] = "Teksheryy"
    session = request.session

    if request.method == "POST":
        form = TempForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            message = form.cleaned_data["text"]

            messages.success(request, f"We got your inputs!{email} and {message}")

            return redirect("main_page")
    else:
        form = TempForm()

    return render(request, "student/temp_template.html", {"form": form})


def main_page(request):
    count = request.session.get("visits", 0)
    request.session["visits"] = count + 1
    request.session.set_expiry(10)
    login = request.session.get("login", False)
    
    if not login:
        request.session["login"] = True
    else:
        print("you are logged in")
    return render(request, "student/main_page.html", {"count": count + 1})
