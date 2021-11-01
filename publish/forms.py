from generic.forms import *
from .models import *

class ArtworkForm(ModelForm, StyledForm):

    class Meta:
        model = ArtWork
        fields = [
            "title",
            "description",
            "file",
            "cover"
        ]
