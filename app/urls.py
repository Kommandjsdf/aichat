from django.urls import path
from . import views
from .views import signup

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup', views.signup, name = "signup")
]