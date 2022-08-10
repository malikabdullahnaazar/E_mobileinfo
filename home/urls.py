from .import views
from django.urls import path

urlpatterns = [
    path("", views.index,name="index"),
    path("signin/", views.signin,name="signin"),
    path("signup/", views.signup,name="signup"),
    path("About/", views.about,name="about"),
]