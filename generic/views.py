from django.urls import reverse_lazy
from django.shortcuts import render, redirect,  get_object_or_404

from django.core.paginator import Paginator
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from django.forms import *

from django.views.generic import *
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin

from json import loads
#from junctions.settings import SETTINGS_REDIRECT_URL


class ManagerAccess(UserPassesTestMixin):
    def test_func(self):
        try:
            access = self.request.user.id == self.get_object().manager.id
            return access
        except KeyError:
            access = self.request.user.id == self.get_object().office.manager.id
            return access

class SuccessUrl:
    """Base redirect link for successful post requests.
    """
    success_url = reverse_lazy("home:home")
    pass

class AddMeta(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta"] = self.meta
        return context


class UserChildView(DetailView, MultipleObjectMixin):
    model = User

    def get_context_data(self, **kwargs):
        manager = self.get_object()
        context = super().get_context_data(object_list=self.child_model.objects.filter(manager=manager, publish=True), **kwargs)
        return context



class UserFormsetView(AddMeta, SuccessUrl, LoginRequiredMixin, FormView):
    """Creates a formset object and then creates it using a user instance.
    """
    template_name = "formset.html"

    def get_form(self, **kwargs):
        form = self.formSet(instance=self.request.user)
        return form
    

    
    def post(self, request, **kwargs):
        user_response = self.formSet(self.request.POST, self.request.FILES, instance=self.request.user)
        if user_response.is_valid():
            user_response.save()
            return redirect(super().success_url)
        else:
            return render(request, self.template_name, {'form':user_response, 'meta': self.meta})



class UserChildFormSet(ManagerAccess, AddMeta, LoginRequiredMixin, UpdateView):
    # model = Office
    template_name = "formset.html"

    def get_form(self, **kwargs):
        form = self.formSet(instance=self.get_object())
        return form


    def post(self, request, *args, **kwargs):
        user_response = self.formSet(self.request.POST, self.request.FILES, instance=self.get_object())
        if user_response.is_valid():
            user_response.save()
            return redirect("office:details", self.get_object().slug)
        else:
        	return render(request, self.template_name, {'form':user_response, 'meta': self.meta})
