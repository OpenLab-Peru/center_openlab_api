# Python imports


# Django imports
from django.db import models
from django.utils import timezone

# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Person(TimeStampedModel):
    SEX_CHOICES = (
        ('0', 'Femenino'),
        ('1', 'Masculino'),
    )

    name = models.CharField(max_length=100)
    last_name_mother = models.CharField(max_length=100)
    last_name_father = models.CharField(max_length=100)
    born_date = models.DateField(blank=True, null=True)
    sex = models.CharField(blank=True, choices=SEX_CHOICES, max_length=1)

    def __str__(self):
        return '{0} {1}, {2}'.format(
            self.last_name_father, self.last_name_mother, self.name)

    def full_name(self):
        return self.__str__()

    @property
    def age(self):
        today = timezone.now().date()
        if self.born_date:
            return today - self.born_date
        else:
            return None
