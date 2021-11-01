from generic.views import *
from .models import *


class AllFeatures(ListView):
    model = Feature
    template_name = 'all-features.html'


class FeatureDetails(DetailView):
    model = Feature
    template_name = 'feature.html'


class Article(DetailView):
    model = Article
    template_name = 'feature-article.html'