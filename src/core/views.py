from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


import environ

@api_view(["GET"])
def api_root(request, format=None):
    env = environ.Env()
    return Response(env)
