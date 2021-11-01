from generic.forms import *
from .models import *
from django.contrib.auth.forms import *


class StyleForm(Form):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs["class"] = form_control


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
            "is_active",
        ]


class SignInForm(AuthenticationForm):
    class Meta:
        fields = ["username", "password"]


class DetailsChangeForm(StyleForm, UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ["first_name", "last_name", "email"]


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for f in self.fields:
            if f == 'password':
                self.fields[f].widget.attrs['hidden'] = True
                self.fields[f].label = ''
                self.fields[f].help_text = ''


class ChangePasswordForm(StyleForm, PasswordChangeForm):
    class Meta:
        fields = ["old_password", "new_password", "new_password2"]


class DisplaySettingsForm(StyleForm, ModelForm):
    class Meta:
        model = DisplaySetting
        fields = ["dark_mode", "small_text"]
        exclude = ["user"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs["class"] = ''


class ResidenceForm(StyleForm, ModelForm):
    class Meta:
        model = Residence
        exclude = ["user"]


class ComsForm(StyleForm, ModelForm):
    class Meta:
        model = ContactDetail
        exclude = ["user"]
