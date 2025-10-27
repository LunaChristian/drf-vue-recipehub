from http import HTTPStatus

from django.http import Http404, JsonResponse
from rest_framework.views import APIView

from .models import *

# Create your views here.

class Clase_1(APIView):
    def post(self, request):
        pass