from django.db.models import *
from django.urls import reverse
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User


class UserManaged(Model):
    manager = ForeignKey(User, on_delete=CASCADE)

    class Meta:
        abstract = True


class PublicAccess(Model):
    publish = BooleanField(default=True)
    verified = BooleanField(default=False)

    class Meta:
        abstract = True


class Reference(Model):
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Title(Model):
    title = CharField(max_length=255)

    class Meta:
        abstract = True
        ordering = ['title']

    def __str__(self):
        return self.title


class Text(Model):
    description = TextField()

    class Meta:
        abstract = True
    
    def long_description(self):
        if len(self.description) > 90:
            return True
        else:
            return False


class Address(Model):
    street = CharField(max_length=255, blank=True, null=True)
    town = CharField(max_length=255, blank=True, null=True)
    city = CharField(max_length=255, blank=True, null=True)
    province = CharField("Province/State", max_length=255, blank=True, null=True)
    country = CharField(max_length=255, blank=True, null=True)
    code = CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

    def address_as_list(self):
        return [
            self.street,
            self.town,
            self.city,
            self.code,
            self.province,
            self.country,
        ]

    def address_provided(self):
        for item in self.address_as_list():
            if item:
                return True
        else:
            return False

class Contact(Model):
    call = CharField(max_length=255, blank=True, null=True)
    email = EmailField(blank=True, null=True)

    class Meta:
        abstract = True

    def contact_as_list(self):
        if not self.email or self.email == "":
            return [self.call, self.manager.email]
        else:
            return [self.call, self.email]


class SlugifyTitle(Model):
    """Creates a slug from title
    """
    slug = SlugField(max_length=210, unique=True)
    
    class Meta:
        abstract = True

    def save(self, **kwargs):
        self.slug=slugify(self.title)
        return super().save(**kwargs)
