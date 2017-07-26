from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import redirect
from contact.forms import ContactForm
from django.core.mail import send_mail
from django.views.generic import FormView

# Import TemplateView

class  ContactPageView (  FormView  ):
    template_name = 'contact/contactform.html'
    success_url = 'contact/welcome_email.html'
    form_class = ContactForm

    def form_valid(self, form):
        message = "{name} / {email} said: ".format (
            name=form.cleaned_data.get ( 'name' ),
            email=form.cleaned_data.get ( 'email' ) )
        message += "\n\n{0}".format ( form.cleaned_data.get ( 'message' ) )
        send_mail (
            subject=form.cleaned_data.get ( 'subject' ).strip (),
            message=message,
            from_email='contact-form@myapp.com',
            recipient_list=[settings.EMAIL_HOST],
        )
        return super ( ContactPageView, self ).form_valid ( form )
