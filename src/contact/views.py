from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from contact.forms import ContactForm

# Import TemplateView

class ContactPageView ( FormView ):
    template_name = "contact/contactform.html"
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactPageView, self).form_valid(form)
