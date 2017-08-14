from django import forms
from localflavor import generic

class PersonForm(forms.Form):
    phone = generic.forms.PhoneNumberField(blank=True, default='')