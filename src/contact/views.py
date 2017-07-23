from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponseRedirect
from .forms import NameForm

# Import TemplateView

class ContactPageView ( TemplateView ):
    template_name = "contact/contactform.html"

    def get_name(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = NameForm (request.POST or None)
            # check whether it's valid:
            if form.is_valid ():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect ( '/thanks/' )

            else:
                return render ( request, 'contactform.html', dict ( form=form ) )

        # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm ()
            return render ( request, 'contactform.html', dict ( form=form ))
