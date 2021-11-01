from django.contrib.auth.models import User
from django.forms import *


form_control = 'form-control'



class StyledForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs["class"] = form_control