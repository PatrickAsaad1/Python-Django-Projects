from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("members/", views.members, name="members"),
    path("admin/", admin.site.urls),
]
