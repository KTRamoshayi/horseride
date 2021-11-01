from django.contrib.admin import *
from .models import *

class ArtWorkAdmin(ModelAdmin):
    list_display = ['title', 'manager', 'file', 'cover', 'publish', 'verified', 'created', 'modified']
    list_filter = ['manager', 'publish', 'verified']

site.register(ArtWork, ArtWorkAdmin)
