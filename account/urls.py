from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name='account'
urlpatterns = [ #reg
    path('register/', views.register, name='register'),
    path("register_done/", 
    TemplateView.as_view(template_name="account/register_done.html"), 
    name="signup_done"),
    path("login/", views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("edit-profile/",views.edit,name="edit-profile"),
    path("profile-view/<int:pk>",views.user_profile_detail,name="profile-view")

]