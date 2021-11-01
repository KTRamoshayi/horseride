from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path("", LandingPage.as_view(), name="landing-page"),
    path('home', Home.as_view(), name='home')
]
