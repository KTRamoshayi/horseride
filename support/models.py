from generic.models import *
from django.urls import reverse


class Feature(Title, Contact, Text, Reference, SlugifyTitle):
    prepopulated_fields = {"slug": ["title"]}
    slug = SlugField(max_length=210)

    def get_absolute_url(self):
        return reverse('support:feature', args=[str(self.slug)])


class Article(Title, Text):
    feature = ForeignKey(Feature, on_delete=CASCADE)
    caption = CharField(max_length=300)

    class Meta:
        ordering = ['feature', 'title']

    def get_absolute_url(self):
        return reverse('support:article', args=[str(self.id)])
