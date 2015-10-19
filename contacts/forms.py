from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder    
import os

class ContactFormHelper(FormHelper):
    form_tag = False
    form_method = 'get'
    form_class = 'form-inline'
    field_template = os.path.join('bootstrap3','layout', 'inline_field.html')
    layout = Layout(
         'firstName',
         'lastName',
         'state',
         'board',
         'positionHeld',
    )