# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer

# Local imports
from .models import Person, Document


# Create your serializers here.
class PersonModelSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class DocumentModelSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
