from generic.views import *
from .forms import *
from django.contrib.auth.views import *
from horseride.settings import REGISTER_REDIRECT_URL


class UserEdit(LoginRequiredMixin, UpdateView):
    template_name = "accounts-form.html"
    success_url = reverse_lazy("accounts:options")
    
    def get_object(self):
        return self.model.objects.get(user=self.request.user)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "sign-up.html"
    success_url = reverse_lazy(REGISTER_REDIRECT_URL)


class SignInView(LoginView):
    form_class = SignInForm
    template_name = "sign-in.html"


class OptionsView(LoginRequiredMixin, TemplateView):
    template_name = "options.html"


class PasswordChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = "accounts-form.html"

    def get_object(self):
        return self.request.user


class DetailsChangeView(UserEdit):
    model = User
    form_class = DetailsChangeForm

    def get_object(self):
        return self.request.user


class DisplaySettingsView(UserEdit):
    model = DisplaySetting
    form_class = DisplaySettingsForm


class ResidenceView(UserEdit):
    model = Residence
    form_class = ResidenceForm


class ComsView(UserEdit):
    model = ContactDetail
    form_class = ComsForm


class UserPortfolio(DetailView):
    model = User
    template_name = 'user-profile.html'
