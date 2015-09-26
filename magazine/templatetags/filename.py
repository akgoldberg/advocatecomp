import os

from django import template
from django.template.defaultfilters import stringfilter

# gets only the filename from a longer file path
# http://stackoverflow.com/questions/2683621/django-filefield-return-filename-only-in-template

register = template.Library()

@register.filter(name = 'filename')
def filename(value):
    return os.path.basename(value.file.name)
