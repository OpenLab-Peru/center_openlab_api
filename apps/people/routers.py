# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import PersonModelViewSet


# Create your routers here.
router_list = (
    (r'persons', PersonModelViewSet),
)
