from django import forms
from catalog.models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()
    def clean_price(self):
        if self.cleaned_date['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
            return self.cleaned_date['price']

