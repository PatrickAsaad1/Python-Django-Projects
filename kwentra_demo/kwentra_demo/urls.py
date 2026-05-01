from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('admin/', admin.site.urls),
]
