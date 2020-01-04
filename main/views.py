from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from . import models

class HomePage(generic.ListView):
    # Setting model variable lets django send a context dictionary to index.html with all model fields
    model = models.Content 
    template_name = 'main/index.html'