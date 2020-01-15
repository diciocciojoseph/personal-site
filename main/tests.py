from django.test import TestCase


from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage

images = [

    'github_logo.png', 'linkedin_logo.png', 'lol.png', 'portrait.png', 'puzzle.png', 'sample_editor.png',
    'uconn_2022.png', 'uconn_logo.png', 'wethersfield.png',

]

css = [
    'main.css',
]

class TestStaticFiles(TestCase):
    # Check if app contains/loads static files
    def test_images(self):
        for image_name in images:
            abs_path = finders.find('images/' + image_name)
            self.assertTrue(staticfiles_storage.exists(abs_path))

    def test_css(self):
        for sheet_name in css:
            abs_path = finders.find('css/' + sheet_name)
            self.assertTrue(staticfiles_storage.exists(abs_path))