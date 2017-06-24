# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Person


# Register your models here.
@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'sex', 'age')
