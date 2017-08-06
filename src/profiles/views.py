from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class ProtectedView(TemplateView):
    template_name = "profiles/profile.html"

    """@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)"""

    @method_decorator ( login_required )
    def dispatch(self, request, *args, **kwargs):
        return super ( LoginRequiredMixin, self ).dispatch (
            self, request, *args, **kwargs )


    """class MyView ( LoginRequiredMixin, View ):
        login_url = '/login/'
        redirect_field_name = '/login'"""
