from django import forms

class ContactForm(forms.Form):
    name = forms.CharField ( required=True )
    email = forms.EmailField ( required=True )
    subject = forms.CharField ( required=True )
    message = forms.CharField ( widget=forms.Textarea )

    def __init__(self, *args, **kwargs):
        super ( ContactForm, self ).__init__ ( *args, **kwargs )
        self.fields['name'].label = "Your name:"
        self.fields['email'].label = "Your email:"
        self.fields['message'].label = "What do you want to say?"



