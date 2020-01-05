from django.db import models
from django.conf import settings
import os

# Model to facilitate the creation and display of main content cards on the main page
# Can also be used in the future to link sub-content pages in a similar manner with Foreign Keys
# See the index.html file in templates to see how class-based views can be utilized with models
# to display content very easily

def images_path():
    return os.path.join(settings.BASE_DIR, r'main\static\images')

# This content model is used to display the content on cards in the homepage
# for example, each card has an image, title, text and button text as well as a link when clicked.
class Content(models.Model):
    title = models.CharField(max_length=128, default="Title")
    description = models.CharField(max_length=256, default="Description")

    image = models.FilePathField(path=images_path())
    image_path = models.CharField(max_length=128, default="Path")

    link = models.URLField()
    link_text = models.CharField(max_length=64, default="Learn More")

    def __str__(self):
        return self.title

# This model can be implemented to create similar card-like subpages in the future

# class SubContent(models.Model):
#     content = models.ForeignKey(Content, on_delete=models.CASCADE)
#     title = models.CharField()
#     description = models.CharField()
#     image = models.FilePathField(path=images_path())
#     link = models.URLField()
    
