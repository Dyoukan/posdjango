from django import forms

from .models import Regex

class RegexForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    regex_search = forms.CharField(widget=forms.Textarea)
    regex_change = forms.CharField(widget=forms.Textarea)
