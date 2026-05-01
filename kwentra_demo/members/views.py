from django.shortcuts import render


def members(request):
    return render(request, "members.html")


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
