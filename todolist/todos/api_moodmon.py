from django.contrib.auth import login
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from todos.models import FeedBack
import logging

LOGGER = logging.getLogger(__name__)


@api_view(['POST'])
def signinout(request):
    result_respones = ""
    userdata = request.data
    # login()
    if not userdata:
        return result_respones(
            "error",
            "notfound"
        )

    return result_respones(
        "success",
        userdata['username']
    )

