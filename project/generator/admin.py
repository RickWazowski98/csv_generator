from django.contrib import admin
from .models import Schema, SchemaColumn, DataSet


class SchemaColumnInline(admin.StackedInline):
    model = SchemaColumn

@admin.register(Schema)
class SchemaModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'date_of_modified']
    inlines = [SchemaColumnInline, ]

@admin.register(DataSet)
class DataSetModelAdmin(admin.ModelAdmin):
    list_display = ['schema', 'data_of_creation']