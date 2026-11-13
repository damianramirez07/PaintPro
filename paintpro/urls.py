from django.contrib import admin
from django.urls import path
# imports dashboard
from core import views

urlpatterns = [
    path ('admin/', admin.site.urls), # admin interface
    path('', views.dashboard, name='dashboard'), # displays dashboard

]