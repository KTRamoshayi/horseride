from django.urls import path
from .views import *

app_name = "support"

urlpatterns = [
    path('features', AllFeatures.as_view(), name='all-features'),
    path('feature/<slug:slug>', FeatureDetails.as_view(), name='feature'),
    path('article/<int:pk>', Article.as_view(), name='article'),
    #path("management/<slug:slug>", BranchManagement.as_view(), name="management"),
]