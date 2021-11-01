from generic.models import *


class ArtWork(UserManaged, Title, Text, Reference, PublicAccess):
    file = FileField(upload_to='file/%Y/%m/%d/')
    cover = ImageField(upload_to='cover/%Y/%m/%d/')

    class Meta:
        ordering = ["manager"]

