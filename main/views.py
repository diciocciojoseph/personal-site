from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from . import models

# Class based list view simply displays all models on the page in a list
# We can specify the way they are displayed in the template file
# Note: all fields in the model are automatically passed as context to the template

class HomePage(generic.ListView):
    # Setting model variable lets django send a context dictionary to index.html with all model fields
    model = models.Content 
    template_name = 'main/index.html'