from django.contrib import admin
from . import models

# Register models so we can add/modify them easily in the django admin page

admin.site.register(models.Content)