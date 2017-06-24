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

    born_date = models.DateField(blank=True, null=True)
    cellphone = models.CharField(blank=True, max_length=9)
    email = models.EmailField()
    last_name_father = models.CharField(max_length=100)
    last_name_mother = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sex = models.CharField(blank=True, choices=SEX_CHOICES, max_length=1)

    class Meta:
        verbose_name = 'Persona'

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


class Document(models.Model):
    DOCUMENT_CHOICES = (
        ('0', 'DNI'),
        ('1', 'Pasaporte'),
        ('2', 'Carnet de Extranjeria'),
        ('3', 'Carnet Universitario'),
    )

    kind = models.CharField(choices=DOCUMENT_CHOICES, max_length=1)
    person = models.ForeignKey('Person')
    value = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Documento'

    def __str__(self):
        return '{0} {1}, {2}'.format(
            self.person.last_name_father, self.person.last_name_mother,
            self.person.name)
