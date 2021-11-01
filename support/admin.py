from django.contrib.admin import *
from .models import *


class FeatureAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ['title', 'call', 'email']
    list_filter = ['title', 'call', 'email']

site.register(Feature, FeatureAdmin)


class ArticleAdmin(ModelAdmin):
    list_display = ['feature', 'title']
    list_filter = ['feature', 'title']

site.register(Article, ArticleAdmin)
