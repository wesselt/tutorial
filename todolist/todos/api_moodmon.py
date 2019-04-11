from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

import logging

LOGGER = logging.getLogger(__name__)

@api_view(['POST'])
def signinout(request):
    host = request.data

    if not hosts:
        return result_respones(
            "warning",
            "Geen host gevonden"
        )

    return result_respones(
        "success",
        hosts
    )





