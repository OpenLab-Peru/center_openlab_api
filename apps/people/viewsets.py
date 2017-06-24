# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Person
from .serializers import PersonModelSerializer


# Create your viewsets here.
class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
