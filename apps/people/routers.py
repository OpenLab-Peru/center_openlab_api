# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import PersonModelViewSet, DocumentModelViewSet


# Create your routers here.
router_list = (
    (r'document', DocumentModelViewSet),
    (r'people', PersonModelViewSet),
)
