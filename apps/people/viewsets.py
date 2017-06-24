# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet

# Local imports
from .models import Person, Document
from .serializers import PersonModelSerializer, DocumentModelSerializer


# Create your viewsets here.
class PersonModelViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer


class DocumentModelViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentModelSerializer
