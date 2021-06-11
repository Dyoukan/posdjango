from django import forms

from .models import Regex

class RegexForm(forms.Form):
    name = forms.CharField(max_length=20)
    regex_search = forms.TextInput()
    regex_change = forms.TextInput()