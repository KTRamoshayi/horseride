from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path("", OptionsView.as_view(), name="options"),
    path("sign-up", SignUpView.as_view(), name="sign-up"),
    path("sign-in", SignInView.as_view(), name="sign-in"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("password-change", PasswordChangeView.as_view(), name="password-change"),
    path("details-change", DetailsChangeView.as_view(), name="details-change"),
    path("residence", ResidenceView.as_view(), name="residence-change"),
    path("coms", ComsView.as_view(), name="coms-change"),
    path(
        "display-settings",
        DisplaySettingsView.as_view(),
        name="display-settings",
    ),
    
    path("<int:pk>", UserPortfolio.as_view(), name="portfolio")
]
