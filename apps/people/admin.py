# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Person, Document


# Register your models here.
@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sex', 'age',)


@admin.register(Document)
class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ('value', 'kind',)
