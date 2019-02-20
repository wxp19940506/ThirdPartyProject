from django.db import models
from tinymce.models import HTMLField

class RichText(models.Model):
    content = HTMLField()

