from django import forms

from pregunkane.models import Frase

class FraseForm(forms.ModelForm):
    class Meta:
        model = Frase
        exclude = ('data',)
