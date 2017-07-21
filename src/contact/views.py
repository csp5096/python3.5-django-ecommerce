from django.shortcuts import render, get_object_or_404
#from contact.models import Contact
from django.views.generic import TemplateView, RedirectView
# Import TemplateView

class ContactPageView(TemplateView):
    template_name = "contact/forms.html"
