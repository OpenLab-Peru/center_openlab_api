# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer

# Local imports
from .models import Person


# Create your serializers here.
class PersonModelSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
