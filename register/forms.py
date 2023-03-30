from django import forms


class RegForm(forms.Form):
    company_name = forms.CharField()
    number_attending = forms.IntegerField()
    date = forms.DateField()
