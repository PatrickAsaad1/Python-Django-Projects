from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


@login_required
def services(request):
    return render(request, "services.html")


@login_required
def contact(request):
    return render(request, "contact.html")


@login_required
def members(request):
    return render(request, "members.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def error_404(request, exception):
    return render(request, "404.html", status=404)
