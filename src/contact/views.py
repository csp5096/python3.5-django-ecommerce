from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from contact.forms import ContactForm
from emailtools import HTMLEmail

# Import TemplateView

class  ContactPageView (  FormView  ):
    template_name = 'contact/contactform.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactPageView, self).form_valid(form)

class WelcomeEmail(HTMLEmail):
    template_name = 'contact/welcome_email.html'
    from_email = 'admin@example.com'
    to_email = [settings.EMAIL_HOST_USER]
    subject = 'Welcome to example.com'

    def get_to(self):
        return [self.args[0].email]

    def get_context_data(self, **kwargs):
        kwargs = super(WelcomeEmail, self).get_context_data(**kwargs)
        kwargs['user'] = self.args[0]
        return kwargs