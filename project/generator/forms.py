from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from .models import Schema, SchemaColumn
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class SchemaColumnForm(forms.ModelForm):
    class Meta:
        model = SchemaColumn
        exclude = ()

class SchemaForm(forms.ModelForm):

    class Meta:
        model = Schema
        exclude = []

    def __init__(self, *args, **kwargs):
        super(SchemaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('column_separator'),
                Field('string_character'),
                Fieldset('Add column',
                    Formset('columns')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save', )),
                )
            )

SchemaColumnFormSet = inlineformset_factory(
    Schema,
    SchemaColumn,
    form=SchemaColumnForm,
    fields=['column_name', 'column_type', 'order'],
    can_delete=True,
)