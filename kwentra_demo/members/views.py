from django.shortcuts import render


def members(request):
    return render(request, "members.html")


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


def error_404(request, exception):
    return render(request, "404.html", status=404)
