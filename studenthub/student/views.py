from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from student.forms import UserRegisterForm, UserLoginForm

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

@login_required(login_url="login")
def main_page(request):
    count = request.session.get("visits", 0)
    request.session["visits"] = count + 1
    request.session.set_expiry(10)
    login = request.session.get("login", False)
    request.session["soma_data"] = {"info": [232, 51, 513]}

    # cookies
    temp = request.COOKIES.get("temp", "jok")
    temp2 = request.COOKIES.get("brauzer", "GERE")
    if not login:
        request.session["login"] = True
    else:
        print("you are logged in")
    return render(
        request,
        "student/main_page.html",
        {"count": count + 1, "login": login, "cookie": temp2},
    )


#  cocik


def temp_cookies(request):
    response = HttpResponse("Bizdin cookies response")

    response.set_cookie("temp", "hello world", max_age=120)

    response.set_cookie("DARK_mode", "1", max_age=60)

    return response


#  authentication


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(form.cleaned_data["password"])

            user.save()

            messages.success(request, "siz registration bolduhuz! login bolohuz!")
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "student/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

            messages.success(request, "siz login bolduhuz! login bolohuz!")
            return redirect("main_page")
        else:
            messages.error(request, "tura emes username jana password ")
    else:
        form = UserLoginForm()

    return render(request, "student/login.html", {"form": form})


def logout_view(request):

    logout(request)

    messages.info(request, "siz logout bolduhuz! login bolohuz!")
    return redirect("login")
