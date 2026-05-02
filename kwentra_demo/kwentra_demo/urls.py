from django.contrib import admin
from django.urls import path
from members import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("members/", views.members, name="members"),
    path("admin/", admin.site.urls),
    # Authentication
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
