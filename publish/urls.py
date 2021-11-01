from django.urls import path
from .views import *

app_name = 'publish'



urlpatterns = [
    path('details/<int:pk>', ArtworkDetails.as_view(), name='artwork-details'),
    path('list/<int:pk>', UserArtworkList.as_view(), name='user-artwork-list'),
    path('management', ArtworkManagement.as_view(), name='management')
]
