from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .fields import OrderField


class Schema(models.Model):
    COLUMN_SEPARATORS = [
        (',', 'Comma(,)'),
        (';', 'Semicolon(;)'),
    ]
    STRING_CHARACTERS = [
        ('\"', 'Double-quote(\")'),
        ('\'', 'Single-quote(\')'),
    ]

    name = models.CharField(max_length=200, default='')
    column_separator = models.CharField(choices=COLUMN_SEPARATORS, default=',', max_length=2)
    string_character = models.CharField(choices=STRING_CHARACTERS, default='\"', max_length=2)
    date_of_modified = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class SchemaColumn(models.Model):
    COLUMN_TEPES = [
        ('full_name', 'Full name'),
        ('job', 'Job'),
        ('email', 'Email'),
        ('phone_number', 'Phone number'),
        ('address', 'Address'),
        ('date', 'Date'),
        # ('integer', 'Integer'),
        ('text', 'Text'),
    ]
    schema = models.ForeignKey(Schema, related_name='columns', on_delete=models.CASCADE)
    column_name = models.CharField(max_length=200)
    column_type = models.CharField(choices=COLUMN_TEPES, default='full_name', max_length=12)
    order = OrderField(blank=True, for_fields=['schema',])

    def __str__(self):
        return self.column_name


class DataSet(models.Model):
    schema = models.ForeignKey(Schema, related_name='schema', on_delete=models.CASCADE)
    data_of_creation = models.DateField(auto_now_add=True)
    file = models.FileField(storage=FileSystemStorage(location='static/csv_files'))

    def __str__(self):
        return self.schema.name
