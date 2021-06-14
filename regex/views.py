from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic

from regex.forms import RegexForm

# Create your views here.
class IndexView(generic.FormView):
    template_name = "regex/index.html"
    form_class = RegexForm

def index(request):
    return HttpResponse("AAA")